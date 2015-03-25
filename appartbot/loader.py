
import logging
from classmanager import class_loader
from modules.module import Module
from queue import Queue,Empty
import os

class Bot:
	def __init__(self, tweet, host, port, log):
		self.host = host
		self.port  = port
		self.tweet = tweet
		self.logging = log
		self.queue = Queue()
		
		self._load_all_missions("maison")
	
	def _load_all_missions(self, prefix):
		path = os.path.join(os.getcwd(), "modules", prefix)
		modules = set(class_loader(path))
		self.modules = []
		for module in modules:
			if module.__name__ != "Module" and issubclass(module, Module):
				m = module(self)
				self.modules += [m]
				self.logging.warn('module %s loaded ...' % m.__class__.__name__)
				
	def getmsg(self):
		while True:
			try:
				q = self.queue.get(False) #non blocking
			except Empty:
				q = None
			yield q
				
	def run(self):
		for msg in self.getmsg():
			for mod in self.modules:
				if mod.event(msg):
					mod.action(msg)
		return 0


