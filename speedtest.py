#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

#Global Config

# Fake Speedtest result for debugging.
fakeSpeedtestResult = 1
# Fake ping result for debugging.
# 1 for Debian, 2 for Windows, 3 for OS X.
fakePingResult = 2
# Fake yeelink.com post status.
# 0 to disable. An HTTP response code (e.g. 200) will enable this option.
fakePostStatus = 200
# Output detailed debug message.
verboseMode = 1
# Log level setting
# All level < logLevel won't be shown.
# 0 = info
# 1 = warning
# 2 = error
# 3 = fatal error
logLevel = 0
# Output every system command call. Default log level is info(0).
showCommandOutput = 1
pingServerName = "itunes.apple.com"

# Global variables (DO NOT MODIFY!)
logSerial = 0

# Strings
logLevelString = {
    0:"Info",
    1:"Warning",
    2:"Error",
    3:"Fatal Error"
    }

import os
import httplib
import socket
import sys
import datetime
import re

from config import config
from debugConfig import debugString
from commonlib import *


def getCurrentTime():
    '''Return a string for current time.'''
    return str(datetime.datetime.now())

def log(context, level = 0):
    '''Print out log text when verbose mode enabled.

Log level definition:

0 = info
1 = warning
2 = error
3 = fatal error
'''
    if (verboseMode == 0 or level < logLevel):return 0
    global logSerial
    logSerial = logSerial + 1
    time = getCurrentTime()
    for line in str(context).split("\n"):
        if line == "": print_("\n")
        else: print_(logLevelString[level] + "[" + str(logSerial) + ":" + time + "]" + line)
    return 0

def post_data1(sensor_id, data):
    '''Post data to yeelink.com'''
    d = '{"value": %f}' % data
    h = {"U-ApiKey": config.API_KEY}
    p = "/v1.0/device/%d/sensor/%d/datapoints" % (config.device_id, sensor_id)
    conn = httplib.HTTPConnection("api.yeelink.net", timeout=30)
    conn.request("POST", p, d, h)
    response = conn.getresponse()
    return response.status

def post_data(sensor_id, data):
    '''post_data wrapper. Prevent timeout to cause the function never returns.'''
    if fakePostStatus != 0:
        return fakePostStatus
    try:
        r = post_data1(sensor_id, data)
    except (httplib.HTTPException, socket.error) as e:
        log("HTTP Request failed.")
        return -1
    return r

def readCommandOutput(command):
    '''Read the output of a command.'''
    if showCommandOutput != 0:
        log("Running command: " + command)
    result = os.popen(command).read()
    if showCommandOutput != 0:
        log("Command output:\n" + result)
    return result

def pingServer(server, count = 10 ):
    '''Actual ping and return results.'''
    #TODO: add count support and cross-platform support
    if fakePingResult == 0:
        return readCommandOutput('ping ' + server)
    else:
        try:
            return debugString.pingResult[fakePingResult-1]
        except e:
            #TODO: Add a good error hint
            sys.exit(1)

def execPing():
    '''Ping and process data'''
    log("Starting ping test...")
    output = pingServer(pingServerName)
    result = {}
    try:
        (result["server"], result["ip"], result["dataLength"]) = re.findall(r'''
                   Ping\s                                 # Case insensitive "Ping"
                   (.*)                                   # Server real domain
                   \s                                     # A space
                   [\[\(]                                 # IP starts with a "[" or "("
                   (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})     # IP address
                   [\]\)]                                 # IP ends with a "]" or ")"
                   \D+                                     # Any char here, as long as it isn't a number
                   (\d{1,4})                              # Data length
                   [\s\(]                                 # Data length ends with a space or "("
                   ''', output, re.IGNORECASE + re.VERBOSE)[0]
        result["lostPercent"] = re.findall(r'''
                    (\d+\.?\d{0,2}%)                       # Package lost percent
                    ''', output, re.VERBOSE)[0] # Original: (\d+\.?\d{0,2}%) 
        a = re.findall(r'''
                    %.*
                    =\s
                    (\d+\.?\d*)\D+
                    (\d+\.?\d*)\D+
                    (\d+\.?\d*)\D+
                    (.*)
                    ms
                    ''', output, re.IGNORECASE + re.DOTALL + re.VERBOSE)
##r'''
##                    =\s
##                    (\d+\.?\d{0,3})\D+
##                    (\d+\.?\d{0,3})\D+
##                    (\d+\.?\d{0,3})\D+
##                    (\d+\.?\d{0,3})
##                    ms
##                    '''
    except IndexError as e:
        log("Ping result process failed.", 2)
        raise e
    
    print a
    # Exit here: for debug purpose
    sys.exit(1)
    ping = ping.split("\n")
    loss = float(ping[-3].split(" ")[5].replace("%", ""))
    (tmin, tavg, tmax, tstddev) = tuple(ping[-2].split(" ")[3].split("/"))
    log("Uploading data...")
    log("===Packet loss===")
    log(post_data(13472, float(loss)))
    log("===tmin===")
    log(post_data(13473, float(tmin)))
    log("===tavg===")
    log(post_data(13474, float(tavg)))
    log("===tmax===")
    log(post_data(13475, float(tmax)))
    log("===tstddev===")
    log(post_data(13476, float(tstddev)))
    return 0

def speedtest():
    '''Test speed.'''
    res = ''
    log("Running speed test, please wait...", 0)
    execPing()

    if fakeSpeedtestResult != 0:
        res = debugString.speedtestResult[fakeSpeedtestResult - 1]
    else:
        res = readCommandOutput("python ./speedtest-cli.py --simple")
        
    try:
        resu = res.split("\n")
        ping = float(resu[0].split(": ")[1].split(" ")[0])
        down = float(resu[1].split(": ")[1].split(" ")[0]) / 8. * 1024
        up = float(resu[2].split(": ")[1].split(" ")[0]) / 8. * 1024
    except (httplib.HTTPException, socket.error) as e:
        ping = 0
        down = 0
        up = 0

    output = '网速测试结果：\n连接时间：%0.3f 毫秒\n下载速度：%0.2f KB/s\n上传速度：%0.2f KB/s' % (ping, down, up)
    log(output)
    log("Uploading data...")
    resp = post_data(config.sensor['ping'], ping)
    log("===Ping===")
    log(resp)
    resp = post_data(config.sensor['download'], down)
    log("===Download===")
    log(resp)
    resp = post_data(config.sensor['upload'], up)
    log("===Upload===")
    log(resp)
    log("Finished.")

    log("All tasks finished.")

def printConfig():
    log("Speedtest Command Wrapper " + __version__, 0)
    log("by " + __author__, 0)
    log("==========Config==========")
    log("Fake Speedtest Result: " + str(bool(fakeSpeedtestResult != 0)), 0)
    if fakeSpeedtestResult != 0:log("Use Speedtest Result Preset: " + str(fakeSpeedtestResult))
    log("Fake Ping Result: " + str(bool(fakePingResult != 0)), 0)
    if fakePingResult != 0:log("Use Fake Ping Preset: " + str(fakePingResult))
    log("Fake Post Status: " + str(bool(fakePostStatus != 0)), 0)
    if fakePostStatus != 0:log("Use Fake Post Status: " + str(fakePostStatus))
    log("Verbose Mode: " + str(bool(verboseMode == 1)), 0)
    log("Min Log Level: "+ logLevelString[logLevel], 0)
    log("Show Command Output: " + str(bool(showCommandOutput == 1)), 0)
    log("Ping Server Name: " + pingServerName, 0)

def main():
    '''Launch a full speedtest'''
    try:
        printConfig()
        speedtest()
    except KeyboardInterrupt:
        log("\nUser Keyboard Interrupt.", 3)

if __name__ == '__main__':
    main()
