#!/usr/bin/python3

import threading
from socket import *
import time
import logging
import queue
from message import *

class MsgGetter(threading.Thread):
	
	def __init__(self, bot):
		super().__init__()
		self.bot = bot
		self.ip = self.bot.host
		self.port = self.bot.port
		self.logging = self.bot.logging
		self.queue = self.bot.queue
		
		ADDR = (self.ip, self.port)
		self.sock = socket(AF_INET, SOCK_STREAM)
		self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.sock.bind(ADDR)
		self.sock.listen(5)
	
	def run(self):
		while True:
			con, client = self.sock.accept()
			data = con.recv(16)
			self.logging.warn(data)
			m = Msg(returnDict(data))
			self.queue.put(m)
			#listen socket
		
		
def main():
	th = MsgGetter(bot)
	th.start()
	
	while True:
		print('coucou')
		time.sleep(2)
		
		
if __name__ == '__main__':
    main()
