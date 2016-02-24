#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8888, type=int)

import sys
sys.path.append('/root/docker.meweb/dockerapi')
from Containers import DockerContainer

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        dc = DockerContainer()

        self.render('index.html', containers=dc.ps())

    def post(self):
        dc = DockerContainer()
        
        action = self.get_argument('action', '')
        cid = self.get_argument('cid', '')

        if action == 'start':
            dc.start(cid)
            self.get()
        elif action == 'stop':
            dc.stop(cid)
            self.get()


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application( handlers=[
        (r'/', IndexHandler)], 
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        template_path=os.path.join(os.path.dirname(__file__), "templates"))
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
