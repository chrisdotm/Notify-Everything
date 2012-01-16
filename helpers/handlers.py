#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import tornado.web
import tornado.template
import os


template_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "views")

class MainHandler(tornado.web.RequestHandler):
    loader = tornado.template.Loader(template_dir)
    def get(self):
        self.write(self.loader.load("base.html").generate())

class AuthHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('.login.')

class NotifierHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('.normal.')
