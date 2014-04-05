#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

# Net stats
# see http://www.netindex.com/

import httplib
import socket
import urllib2
import re

from commonlib import *
from debugConfig import debugString
from config import Config

__all__=["Netindex"]

class Netindex:
    def __init__(self):
        self.url_homepage = Config.netindexUrl
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
        self.headers = {'User-Agent': self.user_agent}

    def get(self):
        log("GET " + self.url_homepage, logLevel.INFO)

        if Config.fakeNetindexStatus == 0:
            try:
                request = urllib2.Request(url=self.url_homepage, headers=self.headers)
                response = urllib2.urlopen(request, timeout=30)
                log("HTTP Response:%s" % response.getcode(), logLevel.INFO)
                #log("Response context:\n" + response.read(), logLevel.DEBUG)
                result = response.read().decode("utf8")
            except (httplib.HTTPException, socket.error) as e:
                log("HTTP Request failed.", logLevel.ERROR)
                return -1
        else:
            result = debugString.netindexResult[Config.fakeNetindexStatus-1]
 
        return self.process_data_all(result)

    def process_data_all(self, data):
        pattern = r'<div class="figure figure-large">\n.*<b class="figure-content">(\d+\.?\d*)</b>'
        try:
            a = float(re.findall(pattern, data)[0]) / 8 * 1024
            log("Average net speed: %.2fKB/s" % a, logLevel.INFO)
            return a
        except (NameError, KeyError) as e:
            log("HTTP Request failed.", logLevel.ERROR)
            return -1

def main():
    # debug purpose only.
    try:
        s = Netindex()
        s.get()
    except KeyboardInterrupt:
        log("\nUser keyboard interrupt. Program terminated.", logLevel.FATALERROR)

if __name__ == '__main__':
    main()
