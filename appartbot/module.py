#!/usr/bin/python3

class Module:
	def __init__(self, bot):
		self.state = 'off'
		self.bot = bot
		
	def event(self, msg):
		return False
		
	def action(self, msg):
		raise NotImplementedError()
		

