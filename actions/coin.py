import random

class coin:

    def __init__(self):
        self = []

    def getAction(self, data):
        ret = int(random.random()*10)
        print ret
        thecoin = 'The coin lands on it\'s SIDE!!!'
        if ret >= 6:
           thecoin = "The coin lands on HEAD."
        else:
           thecoin = "The coin lands on TAILS."
        channel = data.params[0:data.params.index(' ')]
        return 'PRIVMSG ' + channel + ' :' + thecoin
