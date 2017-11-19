"""
设置路由
"""
from handlers import index, login, logout
from handlers.console import index as console_index


uris = [(r'/', index.IndexHandler)]
uris.append((r'/login', login.LoginHandler))            # 登录
uris.append((r'/logout', logout.LogoutHandler))         # 登出



# 网站后台
uris.append((r'/console', console_index.IndexHandler))   # 后台
