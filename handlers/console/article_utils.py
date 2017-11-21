from bson.objectid import ObjectId
import time

async def get_published_article_list(async_db):
    """获取所有已经发表的文章
    """
    articles = async_db.articles.find({"status": 1})
    documents = []
    while await articles.fetch_next:
        doc = articles.next_object()
        doc['_id'] = str(doc['_id'])
        doc['publish_at'] = doc['publish_at'][0].isoformat()
        documents.append(doc)
    return documents

async def id_titles_saved(async_db):
    """获取未发表文章列表
    """
    docs = async_db.articles.find({"status": 0})
    id_titles = []
    while await docs.fetch_next:
        doc = docs.next_object()
        id_titles.append((str(doc['_id']), doc['title']))
    return id_titles

async def get_article_info_by_id(async_db, id):
    """根据id获取文章
    """
    document = await async_db.articles.find_one({"_id": ObjectId(id)})
    document['_id'] = str(document['_id'])
    if 'publish_at' in document:
        document['publish_at'] = document['publish_at'][0].isoformat()
    return document

async def update_article_info_by_id(async_db, id, document):
    """根据id更新文章
    """
    await async_db.articles.update({"_id": ObjectId(id)}, document)  # upsert=True

async def new_article(async_db, create_at):
    """新建一个文章
    """
    await async_db.articles.insert_one({"status": 0, "create_at": create_at, "title": "无标题文章",
                                        "tags": [], "body":"",  "view":""})