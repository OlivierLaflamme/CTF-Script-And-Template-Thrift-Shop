int udp_master(dthread_t *thread)
{
    if (thread == NULL || thread->data == NULL) {
        return KNOT_EINVAL;
    }

    iohandler_t *handler = (iohandler_t *)thread->data;
    int thread_id = handler->thread_id[dt_get_id(thread)];

    if (handler->server->n_ifaces == 0) {
        return KNOT_EOK;
    }

    /* Set thread affinity to CPU core (same for UDP and XDP). */
    unsigned cpu = dt_online_cpus();
    if (cpu > 1) {
        unsigned cpu_mask = (dt_get_id(thread) % cpu);
        dt_setaffinity(thread, &cpu_mask, 1);
    }

    /* Choose processing API. */
    udp_api_t *api = NULL;
    if (is_xdp_thread(handler->server->ifaces, thread_id)) {
#ifdef ENABLE_XDP
        api = &xdp_recvmmsg_api;
#else
        assert(0);
#endif
    } else {
#ifdef ENABLE_RECVMMSG
        api = &udp_recvmmsg_api;
#else
        api = &udp_recvfrom_api;
#endif
    }
    void *rq = api->udp_init();

    /* Create big enough memory cushion. */
    knot_mm_t mm;
    mm_ctx_mempool(&mm, 16 * MM_DEFAULT_BLKSIZE);

    /* Create UDP answering context. */
    udp_context_t udp = {
        .server = handler->server,
        .thread_id = thread_id,
    };
    knot_layer_init(&udp.layer, &mm, process_query_layer());

    /* Allocate descriptors for the configured interfaces. */
    void *xdp_socket = NULL;
    size_t nifs = handler->server->n_ifaces;
    fdset_t fds;
    if (fdset_init(&fds, nifs) != KNOT_EOK) {
        goto finish;
    }
    unsigned nfds = udp_set_ifaces(handler->server->ifaces, nifs,  & fds , 
                                   thread_id ,  & xdp_socket ); 
    if  ( nfds  ==  0 )  { 
        goto  finish ; 
    } 
    //** AFL defines the variable Shim1 before the main loop**//

    /* Loop until all data is read. */ 
    //** Loop until socket events, receive and process udp data packets **/ 
    for  (;;)  { 
        /* Cancellation point. */ 
        if  ( dt_is_cancelled ( thread ))  { 
            break ; 
        }

        /* Wait for events. */
        fdset_it_t it;
        (void)fdset_poll(&fds, &it, 0, -1);

        // ** AFL:Shim2**/ 
        /* Process the events. */
        for (; !fdset_it_is_done(&it); fdset_it_next(&it)) {
            if (!fdset_it_is_pollin(&it)) {
                continue;
            }
            if (api->udp_recv(fdset_it_get_fd(&it), rq, xdp_socket) > 0) {
                api->udp_handle(&udp, rq, xdp_socket);
                api->udp_send(rq, xdp_socket);
            }
        }

        //** AFL: fuzzer processing complete Shim3**/
    }

finish:
    api->udp_deinit(rq);
    mp_delete(mm.ctx);
    fdset_clear(&fds);

    return KNOT_EOK;
}
