from http import server
import threading
import time
from os import path
import json

main_server = None

class _Handler(server.BaseHTTPRequestHandler):

	def __init__(self, request, client_address, server):
		super().__init__(request, client_address, server)
	
	def do_GET(self):
		return main_server.get(self)



class _Server(threading.Thread):

	def __init__(self, port=8000):
		super().__init__()
		self.port = port
		self.log = []

	def index(self, handler):
		handler.send_response(200)
		handler.send_header('Content-type', 'text/html')
		handler.end_headers()
		with open(path.join(path.dirname(__file__),'index.html'), 'rb') as f:
			handler.wfile.write(f.read())

	def ajax(self, handler):
		timestamp = float(handler.path.split('/')[-1])
		print(timestamp)

		to_send = None

		log_len = len(self.log)

		for i in range(log_len - 1, -1:
			if self.log[i]['timestamp'] <= timestamp:
				to_send = self.log[(i+1):log_len]
				break

		if log_len > 0:
			pass

		obj = {'lastTimestamp': 

		handler.send_response(200)
		handler.send_header('Content-type', 'text/html')
		handler.end_headers()
		handler.wfile.write(json.dumps(obj).encode('utf-8'))

	def get(self, handler):
		if handler.path.startswith('/ajax'):
			return self.ajax(handler)
		return self.index(handler)
	
	def append(self, text, id=0):
		self.log.append({'timestamp': time.time(), 'id': id, 'text': text})

	def run(self):
		global main_server
		main_server = self
		addr = ('', self.port)
		self.httpd = server.HTTPServer(addr, _Handler)
		self.httpd.serve_forever()

