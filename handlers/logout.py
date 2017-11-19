from handlers import base

class LogoutHandler(base.BaseHandler):
    """登出
    """
    def get(self):
        self.clear_cookie("username")
        self.redirect(self.get_argument('next', '/'))