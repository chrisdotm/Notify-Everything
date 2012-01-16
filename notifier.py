#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

import settings
from helpers.handlers import *

define("port", default=settings.APP_PORT, help="set APP_PORT in settings.py", type=int)

def main():
    tornado.options.parse_command_line()
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "media"),
        "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJfdsfjdhfkjYYAEQnp2XdTP1o/Vo=",
        "xsrf_cookies": True,
        "debug": True,
    }
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", AuthHandler),
        (r"/home", NotifierHandler),
        (r"/media", tornado.web.StaticFileHandler,
            dict(path=settings['static_path'])),
    ], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()


