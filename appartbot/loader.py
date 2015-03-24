
import logging
from classmanager import class_loader
from modules.module import Module
from queue import Queue

class Bot:
	def __init__(self, tweet, host, port, log):
		self.host = host
		self.port  = port
		self.tweet = tweet
		self.logging = log
		self.queue = Queue()
		
		self._load_all_missions(maison):
	
	def _load_all_missions(self, prefix):
		path = os.path.join(os.getcwd(), "modules", prefix)
		missions = set(class_loader(path))
		self.missions = []
		for mission in missions:
			if mission.__name__ != "Module" and issubclass(module, Module):
				m = module(tweet, ip)
				self.modules += [m]
				self.logging.warn('module %s loaded ...' % m.__class__.__name__)
				
	def run(self):
		
		return


