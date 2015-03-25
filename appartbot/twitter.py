
import twython
import logging

class twytbot:
    def __init__(self, key, secret, acctok, sectok):
        self.KEY = key
        self.SECRET = secret
        self.ACCESS_TOKEN = acctok
        self.SECRET_TOKEN = sectok
        self.twitter = None

    def authentificate(self):
        self.twitter = twython.Twython(self.KEY, self.SECRET, self.ACCESS_TOKEN, self.SECRET_TOKEN)
        try:
            self.twitter.verify_credentials()
        except Exception as e:
            logging.warn("Twitter log failed %s" % e)
