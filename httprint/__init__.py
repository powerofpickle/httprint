# Written By: Coleman Dill
# Last Change: 27 July 2018

import sys
from .server import _Server
from urllib import request, parse

server = None

class _ExternalServer(object):
	def __init__(self):
		pass
<<<<<<< HEAD
=======

>>>>>>> 2c42cb6fa44c09c184b2f289f894a7b20343bf03


def init(port=8000, is_host=None, global_title='HTTPrint'):
	global server
	server = _Server(port, global_title=global_title)
	server.start()

	old_print = sys.stdout.write
	old_err = sys.stderr.write

	def new_print(text):
		server.append(text)
		old_print(text)

	def new_err(text):
		server.append(text)
		old_err(text)
		
	sys.stdout.write = new_print
	sys.stderr.write = new_err
	
def set_global_title(title):
	server.global_title = title
	
