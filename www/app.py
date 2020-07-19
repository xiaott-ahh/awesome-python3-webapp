#！/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'QiuJun tao'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(text='awesome python')

def hello(request):
	name = request.match_info.get('name')
	text = 'hello' + name
	return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/',index),
	            web.get('/{name}',hello)])
web.run_app(app,host='127.0.0.1',port=9000)
'''
async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
'''