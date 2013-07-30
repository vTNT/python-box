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

    def GET(self):
        todos = db.select(tb, order='finished asc, id asc')
        return render.index(config=config,todos=todos)

class New:

    def POST(self):
        i = web.input()
        db.insert(tb, title=i.title, post_date=datetime.now())
        raise web.seeother('/')
