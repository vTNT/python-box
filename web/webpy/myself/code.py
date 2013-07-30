#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2013-07-30 14:22:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from config.url import urls
import web

app = web.application(urls,globals())

if __name__ == "__main__":
    app.run()
