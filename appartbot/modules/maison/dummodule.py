#!/usr/bin/python3

import time
from modules.module import Module

class Dummy(Module):
    def __init__(self, bot):
        super().__init__(bot)

    def event(self, msg):
        if time.strftime('%H:%M') == '00:58':
            if self.state == 'off':
                self.state = 'done'
                return True
        else: 
            self.state = 'off'
        return False
        

    def action(self, msg):
        self.bot.logging.warn('il est 00:50 !')
        print('lol')
        print(msg)
