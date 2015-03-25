#!/usr/bin/python3

class Msg:
	def __init__(self, args=None):
		self.args = args
		
	def __getattr__(self,attr):
		return self.args[attr]
		
		
def returnDict(msg):
	m = msg.strip().split()
	d = dict()
	for n,i in enumerate(m):
		d["at%i" % n] = i
	return d
	
