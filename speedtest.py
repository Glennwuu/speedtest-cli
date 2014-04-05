#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

#Global Config



# Global variables (DO NOT MODIFY!)
result = {}

# Strings


import httplib
import socket
import sys
import re

from config import Config
from debugConfig import debugString
from commonlib import *

def post_data1(sensor_id, data):
    '''Post data to yeelink.com'''
    d = '{"value": %f}' % data
    h = {"U-ApiKey": Config.API_KEY}
    p = "/v1.0/device/%d/sensor/%d/datapoints" % (Config.device_id, sensor_id)
    conn = httplib.HTTPConnection("api.yeelink.net", timeout=Config.networkTimeout)
    conn.request("POST", p, d, h)
    response = conn.getresponse()
    return response.status

def post_data(sensorId, data):
    '''post_data wrapper. Prevent timeout to cause the function never returns.'''
    if sensorId == 0:
        log("Zero sensor ID, unable to post data.", 1)
        return -1
    if Config.fakePostStatus != 0:
        return Config.fakePostStatus
    try:
        r = post_data1(sensorId, data)
    except (httplib.HTTPException, socket.error) as e:
        log("HTTP Request failed.", 2)
        return -1
    if r != 200:
        log("Network error. Response: " + str(r), 2)
    return r

def pingServer(server, count = 10 ):
    '''Actual ping and return results.'''
    #TODO: add count support and cross-platform support
    if Config.fakePingResult == 0:
        return readCommandOutput('ping -c 10 ' + server)
    else:
        try:
            return debugString.pingResult[Config.fakePingResult-1]
        except e:
            #TODO: Add a good error hint
            sys.exit(1)

def execPing():
    '''Ping and process data'''
    log("Starting ping test...")
    output = pingServer(Config.pingServerName)
    global result
    try:
        (result["server"], result["ip"], result["datalength"]) = re.findall(r'''
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
        result["lostpercent"] = re.findall(r'''
                    (\d+\.?\d{0,2})%                       # Package lost percent
                    ''', output, re.VERBOSE)[0] # Original: (\d+\.?\d{0,2}%)
        #(result["min"], result["avg"], result["max"], result["stddev"]) = tuple(output.split("\n")[-1].split(" ")[3].split("/"))
        #TODO: Debug Value 2 didn't pass.
        (t1, t2, t3, tstddev)  = re.findall(r'''
                    %.*
                    =\s
                    (\d+\.?\d*)\D+
                    (\d+\.?\d*)\D+
                    (\d+\.?\d*)\D+
                    (\d+\.?\d*)\D*
                    ms
                    ''', output, re.IGNORECASE + re.DOTALL + re.VERBOSE)[0]
##r'''
##                    =\s
##                    (\d+\.?\d{0,3})\D+
##                    (\d+\.?\d{0,3})\D+
##                    (\d+\.?\d{0,3})\D+
##                    (\d+\.?\d{0,3})
##                    ms
##                    '''
        if t2<t3:(result["min"], result["avg"], result["max"], result["stddev"]) = (t1, t2, t3, tstddev)
        else:(result["min"], result["avg"], result["max"], result["stddev"]) = (t1, t3, t2, tstddev)
    except IndexError as e:
        log("Ping result process failed.", 2)
        raise e
    result["datalength"] = int(result["datalength"])
    result["lostpercent"] = float(result["lostpercent"])
    result["min"] = float(result["min"])
    result["avg"] = float(result["avg"])
    result["max"] = float(result["max"])
    result["stddev"] = float(result["stddev"])
    #print a
    #print result
    log("Ping Result:\n\tServer: %s\n\tIP: %s\n\tData Length: %dBytes\n\tPacket Lost: %.2f%%\n\tMin: %.3fms\n\tAvg: %.3fms\n\tMax: %.3fms\n\tStddev: %.3fms" % (result["server"], result["ip"], result["datalength"], result["lostpercent"], result["min"], result["avg"], result["max"], result["stddev"]))
    log("Post data: packet lost percentage...", end = "")
    log(post_data(Config.sensor["lostpercent"], result["lostpercent"]), noInfo = True)
    log("Post data: min...", end = "")
    log(post_data(Config.sensor["min"], result["min"]), noInfo = True)
    log("Post data: avg...", end = "")
    log(post_data(Config.sensor["avg"], result["avg"]), noInfo = True)
    log("Post data: max...", end = "")
    log(post_data(Config.sensor["max"], result["max"]), noInfo = True)
    log("Post data: stddev...", end = "")
    log(post_data(Config.sensor["stddev"], result["stddev"]), noInfo = True)
    return 0

def speedtestCli():
    global result
    try:
        if Config.fakeSpeedtestResult != 0:
            output = debugString.speedtestResult[Config.fakeSpeedtestResult - 1]
        else:
            output = readCommandOutput("python ./speedtest_cli.py --simple")
        output = output.split("\n")
        result["ping"] = float(output[0].split(": ")[1].split(" ")[0])
        result["download"] = float(output[1].split(": ")[1].split(" ")[0]) / 8. * 1024
        result["upload"] = float(output[2].split(": ")[1].split(" ")[0]) / 8. * 1024
    except (httplib.HTTPException, socket.error) as e:
        log("Network problem.", 3)
        raise e

    #output = '网速测试结果：\n连接时间：%0.3f 毫秒\n下载速度：%0.2f KB/s\n上传速度：%0.2f KB/s' % (ping, down, up)
    log('Speed Test Result: \n\tPing time: %0.3fms\n\tDownload speed: %0.2fKB/s\n\tUpload speed: %0.2fKB/s' % (result["ping"], result["download"], result["upload"]))
    log("Post data: ping...", end = "")
    log(post_data(Config.sensor['ping'], result["ping"]), noInfo = True)
    log("Post data: download...", end = "")
    log(post_data(Config.sensor['download'], result["download"]), noInfo = True)
    log("Post data: upload...", end = "")
    log(post_data(Config.sensor['upload'], result["upload"]), noInfo = True)

def speedtest():
    '''Test speed.'''
    res = ''
    log("Running ping test, please wait...", 0)
    execPing()
    log("Running speed test, please wait...", 0)
    speedtestCli()
    log("Done.", 0)

def printConfig():
    log("Speedtest Command Wrapper " + __version__, 0)
    log("by " + __author__, 0)
    log("==========Config==========", 0)
    log("Fake Speedtest Result: " + str(bool(Config.fakeSpeedtestResult != 0)), 0)
    if Config.fakeSpeedtestResult != 0:log("Use Speedtest Result Preset: " + str(Config.fakeSpeedtestResult))
    log("Fake Ping Result: " + str(bool(Config.fakePingResult != 0)), 0)
    if Config.fakePingResult != 0:log("Use Fake Ping Preset: " + str(Config.fakePingResult))
    log("Fake Post Status: " + str(bool(Config.fakePostStatus != 0)), 0)
    if Config.fakePostStatus != 0:log("Use Fake Post Status: " + str(Config.fakePostStatus))
    log("Verbose Mode: " + str(bool(Config.verboseMode == 1)), 0)
    log("Min Log Level: "+ logLevelString[Config.logLevel], 0)
    log("Show Command Output: " + str(bool(Config.showCommandOutput == 1)), 0)
    log("Ping Server Name: " + Config.pingServerName, 0)
    log("==========================", 0)

def main():
    '''Launch a full speedtest'''
    try:
        printConfig()
        speedtest()
    except KeyboardInterrupt:
        log("\nUser keyboard interrupt. Program terminated.", 3)

if __name__ == '__main__':
    main()
