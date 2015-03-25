#!/usr/bin/python3

import logging
import loader
from settings import *
from connection import MsgGetter


def main():
	
	bot = loader.Bot("tweet", HOST, PORT, logging)
	th = MsgGetter(bot)
	th.start()
	bot.run()
	
	return 0

if __name__ == '__main__':
	main()

