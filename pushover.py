#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

__all__=["Pushover"]

connTimeout = 30 # seconds

def __postdata(host, uri, header, payload):
    try:
        h = {"Content-Type": "application/x-www-form-urlencoded"}
        p = "/1/messages.json"
        conn = httplib.HTTPSConnection(host, timeout = connTimeout)
        conn.request("POST", uri, payload, header)
        response = conn.getresponse()
    except (httplib.HTTPException, socket.error) as e:
        pass

class Pushover(Object):

    class Message(Object):
        def init(self, user):
            self.user = user
            self.message = ""
    
    def __init__(self, token):
        self.token = token
        self.userlist = []
        self.message = 

    def addUser(user):
        '''Add a user or an group to the user list'''
        self.userlist.append(user)

    def 
    # Unfinished
    def rawsend(token, user, data, title = "", priority = 0, ):
        d = 'token=%s&user=%s' % (token, user)
        
        if r != 200:
            log("Network error. Response: " + str(r), logLevel.ERROR)
        else: r = "OK"
        return r

if __name__ == '__main__':
    p = Pushover("aMtAkJmAGy2r4n5bTgQGJ2hk55jK9B")
    p.
