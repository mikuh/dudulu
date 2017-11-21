"""
设置路由
"""
from handlers import index, login, logout
from handlers.console import index as console_index
from handlers.console import create_aritcle

uris = [(r'/', index.IndexHandler)]
uris.append((r'/login', login.LoginHandler))            # 登录
uris.append((r'/logout', logout.LogoutHandler))         # 登出



# 网站后台
uris.append((r'/console', console_index.IndexHandler))   # 后台


# 写文章
uris.append((r'/article/create/(.*)', create_aritcle.WriteArticleByIdHandlers))   # 根据id写文章
uris.append((r'/article/create', create_aritcle.CreateArticleHandler))      # 创建文章页面
