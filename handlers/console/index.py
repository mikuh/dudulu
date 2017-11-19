import tornado.web

from handlers.base import BaseHandler

__all__ = ['IndexHandler']

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('console/index.html', user_info=self.get_current_user())