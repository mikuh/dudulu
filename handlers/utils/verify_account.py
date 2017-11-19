import functools
import hashlib


def get_md5(password):
    md5 = hashlib.md5()
    md5.update((password + "gauss").encode('utf-8'))
    return md5.hexdigest()


def verify_account_password(method):
    """校验账户密码
    """
    @functools.wraps(method)
    async def wrapper(self, *args, **kw):
        account = self.get_argument('account')
        password = get_md5(self.get_argument('password'))
        result = await self.application.async_db.users.find_one({'password': password, '$or':
            [{'username': account}, {'phone': account}, {'email': account}]})
        if not result:
            return self.render('login.html', title="DeepGuess-登录", error_msg="* 验证未通过，用户名或密码错误。")
        return method(self, *args, **kw)
    return wrapper


