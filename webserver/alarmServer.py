#!/usr/bin/python

"""
Save this file as server.py
>>> python server.py 0.0.0.0 8001
serving on 0.0.0.0:8001

or simply

>>> python server.py
Serving on localhost:8000

You can use this to test GET and POST methods.

"""

import SimpleHTTPServer
import SocketServer
import logging
import simplejson
import time
import sys


if len(sys.argv) > 2:
    PORT = int(sys.argv[2])
    I = sys.argv[1]
elif len(sys.argv) > 1:
    PORT = int(sys.argv[1])
    I = "0.0.0.0"
else:
    PORT = 8000
    I = "0.0.0.0"


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.warning("======= GET STARTED =======")
        logging.warning(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        # logging.warning("======= POST STARTED =======")
        # logging.warning(self.headers)
        # print "got post!!"
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print "post_body(%s)" % (test_data)
        print "==============================="
        # SimpleHTTPServer.SimpleHTTPRequestHandler.do_POST(self)

if __name__ == '__main__':
    Handler = ServerHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "@rochacbruno Python http server version 0.1 (for testing purposes only)"
    print "Serving at: http://%(interface)s:%(port)s" % dict(interface=I or "localhost", port=PORT)
    httpd.serve_forever()