import tornado.web
import os
from uri import handlers





class Application(tornado.web.Application):
    def __init__(self, debug):
        settings = {
            'handlers': handlers,
            'template_path': os.path.join(os.path.dirname(__file__), "templates"),
            'static_path': os.path.join(os.path.dirname(__file__), "static"),
            'cookie_secret': "egEMV+mTSr6475tdduxTYI3i9Inl8UTOgrGTAoQiqLc=",
            'xsrf_cookies': True,
            'login_url': "/login",
        }
        settings.update({'debug': debug})
        # self.graph = Graph("bolt://127.0.0.1:7687", username="neo4j", password="deep")  # neo4j连接
        tornado.web.Application.__init__(self, **settings)



if __name__ == '__main__':
    import base64, uuid
    cookie_secret = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    print(cookie_secret)