#!/usr/bin/python3

import time
from modules.module import Module

class DummyGet(Module):
    def __init__(self, bot):
        super().__init__(bot)

    def event(self, msg):
        if msg is not None:
            return True
        
    def action(self, msg):
        self.bot.logging.warn('le message est :')
        print(msg.at0, msg.at1, msg.at2)
