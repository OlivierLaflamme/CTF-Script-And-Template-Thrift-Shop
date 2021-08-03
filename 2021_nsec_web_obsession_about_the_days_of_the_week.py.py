#!/usr/bin/python3

import os
import sys
from wsgiref.handlers import CGIHandler
from wsgiref.util import request_uri
import random
from datetime import date


if sys.version_info < (3,):
    def b(x):
        return x
else:
    import codecs

    def b(x):
        return codecs.latin_1_encode(x)[0]


def application(environ, start_response):
    status = '200 OK'
    if (os.environ['QUERY_STRING'] == "flag=True"):
       
# WE MAKE SURE THAT WE USE AN ENVIRONMENT VARIABLE
        x = os.environ.get('HTTP_FLAGENABLED')
        if (x == "Enabled"):
            f = open('/usr/share/flag.txt')
            output = f.read()
            f.close()
        else:
            output = "Error, the HTTP_FLAG_ENABLED is not found"
    else:
        people = ["Mitnick","Dade Murphy","Acid Burn","CyberBob","MafiaBoy"]
        image = ['mitnick.jpeg','zerocool.jpeg','kate.jpeg','cyberbob.jpeg','michael.jpeg']
        saint = ["nynex","script kiddies","typos","muffin crumbs in keyboards"]
        output = '''<html>
	<head>
		<style>
body {
background-image:url('/arch.jpg');

background-repeat: no-repeat;
background-size: auto 100%;
background-position:center center;
background-color:black;
background-size:contain;
}

#main{
margin-left:25%;
margin-top:5%;
max-width:50%;
text-align:center;
background:rgba(240,240,240,0.5);

}

#glass{
max-width:45%;

}
		</style>
		</head>
	
	<body>
		<div id='main'>
		<h1> Today is the official day of : ''' + people[date.today().day %5] + ' the patron saint of ' + saint[date.today().month %4] + '''</h1>

                <img src="'''  +image[date.today().day %5] + '''"id='glass'/>
		
		</div>
		
</body>
</html>'''



        #output = "Today is the official day of " + random.choice(people) + " the patron saint of " + random.choice(saint)
        #output = str(os.environ)

    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(b(output))))]

    start_response(status, response_headers)

    return [b(output)]

if __name__ == '__main__':
    CGIHandler().run(application)

