from wsgiref.simple_server import make_server
from objle.webhttp.hello import application

httpd =make_server('',8000,application)
print('server port is 8000')
httpd.serve_forever()