import tornado.web
from handlers import base
class IndexHandler(base.BaseHandler):
    def get(self):
        if self.get_current_user():
            user_info = self.get_current_user()
        else:
            user_info = ''
        self.render('index.html', title="DeepGuess", user_info=user_info)