#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

# Net stats
# http://www.netindex.com/download/4,860/Ningbo/
# Find the following data:
##    <header class="overview-header pure-g-r">
##              <div class="pure-u-3-5">
##                <p class="overview-type">Broadband download</p>
##                <h1 class="overview-heading">Ningbo, China</h1>&nbsp;<div class="tooltip-container">
##                  <button class="icon-info tooltip-toggle text-hide">Info</button>
##                  <div class="tooltip">Results were obtained by analyzing test data between Mar 5, 2014 and Apr 3, 2014. Tests from 30,243 unique IPs have been taken in this city and of 45,389 total tests, 3,467 are being used for the current Index.</div>
##                </div>
##              </div>
##
##              <div class="pure-u-2-5">
##                <div class="figure figure-large">
##                  <b class="figure-content">17.5</b>
##                  <span class="figure-unit">Mbps</span>
##              </div>
##            </header>

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
        self.url_homepage = 'http://www.netindex.com/download/4,860/Ningbo/'
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
        a = float(re.findall(pattern, data)[0]) / 8 * 1024
        log("Average net speed: %.2fKB/s" % a, logLevel.INFO)
        return a

def main():
    try:
        s = Netindex()
        s.get()
    except KeyboardInterrupt:
        log("\nUser keyboard interrupt. Program terminated.", logLevel.FATALERROR)

if __name__ == '__main__':
    main()
