# Written By: Coleman Dill
# Last Change: 27 July 2018

import sys
from .server import _Server
from urllib import request, parse

server = None

class _ExternalServer(object):

	def __init__(self):
		pass


def init(port=8000, is_host=None, global_title='HTTPrint'):
	global server
	server = _Server(port, global_title=global_title)
	server.start()

	old_write = sys.stdout.write

	def new_write(text):
		server.append(text)
		old_write(text)
		
	sys.stdout.write = new_write
	
def set_global_title(title):
	server.global_title = title
	
