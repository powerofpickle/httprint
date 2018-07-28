# Written By: Coleman Dill
# Last Change: 27 July 2018

import sys
from .server import _Server
from urllib import request, parse

def init(port=8000, is_host=True):

	server = _Server(port)
	server.start()

	old_write = sys.stdout.write

	def new_write(text):
		server.append(text)
		old_write(text)
		
	sys.stdout.write = new_write
	
