import tornado.web
from handlers.base import BaseHandler
import datetime, time
from .article_utils import id_titles_saved, get_article_info_by_id, update_article_info_by_id, new_article

__all__ = ['CreateArticleHandler']




class CreateArticleHandler(BaseHandler):
    @tornado.web.authenticated
    async def get(self):
        try:
            id_titles = await id_titles_saved(self.application.async_db)
            document = await get_article_info_by_id(self.application.async_db, id_titles[0][0])
        except:
            return self.redirect('/article/create/new')
        self.render('console/create_article.html',
                    user_info=self.get_current_user(), document=document, id_titles=id_titles)

    @tornado.web.authenticated
    async def post(self):
        """保存文章
        """
        id = self.get_argument('id')
        title = self.get_argument('title')
        tags = self.get_argument('tags').split(',')
        st = self.get_argument('st')
        body = self.get_argument('body')
        try:
            view = self.request.files.get('view')[0]
            with open("./static/images/{}.jpg".format(id), 'wb') as f:
                f.write(view['body'])
        except:
            pass
        document = {
            'title': title,
            'tags': tags,
            'view': id+'.jpg',
            'body': body,
            'status': int(st)
            }
        if st == '1':
            document["publish_at"] = datetime.datetime.now(),

        await update_article_info_by_id(self.application.async_db, id, document)
        self.redirect("/article/create/{}".format(id))


class WriteArticleByIdHandlers(BaseHandler):
    """新建/编辑文章"""
    @tornado.web.authenticated
    async def get(self, id):

        if id == 'new':
            create_at = str(int(time.time()*1000))
            await new_article(self.application.async_db, create_at)
            doc = await self.application.async_db.articles.find_one({"create_at": create_at})
            id = str(doc["_id"])
        id_titles = await id_titles_saved(self.application.async_db)
        document = await get_article_info_by_id(self.application.async_db, id)
        self.render('console/create_article_id.html',
                    user_info=self.get_current_user(), document=document, id_titles=id_titles, id=id)