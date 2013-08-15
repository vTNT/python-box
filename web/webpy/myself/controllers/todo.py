#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 14:37:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import web
from config import settings
from datetime import datetime

render = settings.render
db = settings.db
config = settings.config
tb = 'todo'

class Index:

    def GET(self,page=1):
        page = int(page)
        perpage = 10
        offset = (page-1) * perpage
        todos = db.select(tb, order='finished asc, id asc',offset=offset,limit=perpage)
        postcount = db.query('select count(*) as count from todo')[0]
        pages = postcount.count / perpage
        if postcount.count % perpage > 0:
            pages += 1
        if page > pages:
            raise web.seeother('/')
        else:
            return render.index(config=config,todos=todos,pages=pages)

class New:

    def POST(self):
        i = web.input()
        db.insert(tb, title=i.title, post_date=datetime.now())
        raise web.seeother('/')

#class delete:


class Edit:

    def GET(self, id):
        n = db.select(tb, where='id=$id', vars=locals())
        return render.edit(title=n,config=config)

    def POST(self, id):
        i = web.input()
        title = i['title']
        db.update(tb, title=title, where='id=$id', vars=locals())
        raise web.seeother('/')

class Delete:

    def GET(self, id):
        db.delete(tb, where='id=$id', vars=locals())
        raise web.seeother('/')
        