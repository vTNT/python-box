#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 14:37:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import web
from config import settings
from datetime import datetime
import base

render = settings.render
db = settings.db
config = settings.config
admin = config.admin
pwd = config.password

tb = 'todo'

class Index:

    def GET(self,page=1):
        if not base.logged():
            raise web.seeother('/')
        else:
            page = int(page)
            perpage = 10
            offset = (page-1) * perpage
            todos = db.select(tb, order='finished asc, id asc',offset=offset,limit=perpage)
            postcount = db.query('select count(*) as count from todo')[0]
            pages = postcount.count / perpage
            if postcount.count % perpage > 0:
                pages += 1
            if page > pages:
                raise web.seeother('/main')
            else:
                return render.index(config=config,todos=todos,pages=pages)

class New:

    def POST(self):
        i = web.input()
        db.insert(tb, title=i.title, post_date=datetime.now())
        raise web.seeother('/main')

#class delete:


class Edit:

    def GET(self, id):
        n = db.select(tb, where='id=$id', vars=locals())
        return render.edit(title=n,config=config)

    def POST(self, id):
        i = web.input()
        title = i['title']
        db.update(tb, title=title,post_date=datetime.now(), where='id=$id', vars=locals())
        raise web.seeother('/main')

class Delete:

    def GET(self, id):
        db.delete(tb, where='id=$id', vars=locals())
        raise web.seeother('/main')

class Search:

    def POST(self):
        i = web.input()
        timeafter = i['timeafter']
        timebefore = i['timebefore']
        sql = 'select * from todo where post_date between "%s" and "%s" ' % (timebefore, timeafter)
        todos = db.query(sql)
        num = len(todos)
        return render.search(todos=todos,config=config,num=num)
       # return render.search(timeafter=timeafter,timebefore=timebefore,config=config)

class Login:
    def GET(self):
        if base.logged():
            raise web.seeother('/main')
        else:
            return render.login()

    def POST(self):
        username = web.input().username
        password = web.input().password

        if (password == pwd) and (username == admin):
            web.ctx.session.logined = 1
            raise web.seeother('/main')
        else:
            return "you are wrong!!"

class Logout:
    def GET(self):
        web.ctx.session.kill()
        raise web.seeother('/')
