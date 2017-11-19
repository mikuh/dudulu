from .utils import verify_account
from handlers import base

class LoginHandler(base.BaseHandler):
    """登录
    """
    def get(self):
        self.redirect('/') if self.get_current_user() else self.render('login.html', title="DeepGuess-登录",
                                                                       user_info='', error_msg='')

    @verify_account.verify_account_password
    def post(self):
        next_uri = self.get_argument('next', None)
        remember = self.get_argument("remember", None)
        print(remember)
        self.set_secure_cookie("username", self.get_argument("account"), expires_days=30 if remember else None)
        self.redirect(next_uri if next_uri else "/")




