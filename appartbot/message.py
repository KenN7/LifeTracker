#!/usr/bin/python3

class Msg:
	def __init__(self, args=None):
		self.args = args
		
	def __getattr__(self,attr):
		return self.arg[attr]
		
		
def returnDict(msg):
	
	
	
