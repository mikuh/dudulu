import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
from application import Application

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
define("debug", default=True, help="whether to open debug", type=bool)






if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application(options.debug)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    print("Web service started at http://localhost:{}".format(options.port))
    tornado.ioloop.IOLoop.instance().start()