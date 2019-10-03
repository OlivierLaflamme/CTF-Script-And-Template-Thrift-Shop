'''
The code is very simple, use the pyftpdlib module, import module, instantiate, 
the fifth line is the things you need to define yourself, in order, account,
password, directory location, permissions, anyway, use the highest authority on 
the line, The meaning of the authority represented by the letter can be searched by itself. 
The eighth line also needs to define its own computer ip address, and the port can be run after 
completion. Enter ftp://ip in the browser.
'''

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer=DummyAuthorizer()
authorizer.add_user('zhanghao','mima','.',perm='elradfmw')
handler=FTPHandler
handler.authorizer=authorizer
server=FTPServer(('192.168.27.134',21),handler)
server.serve_forever()
