import tornado.web
import tornado.gen
from handlers import base
from handlers.console.article_utils import get_published_article_list

class IndexHandler(base.BaseHandler):
    async def get(self):
        if self.get_current_user():
            user_info = self.get_current_user()
        else:
            user_info = ''
        documents = await get_published_article_list(self.application.async_db)
        self.render('index.html', title="DeepGuess", user_info=user_info, articles=documents)