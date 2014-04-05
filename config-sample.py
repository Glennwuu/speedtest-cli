#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

class Config:
    '''Config here. Rename it to config.py.'''
    sensor = {}

    # Yeelink API Key
    API_KEY = ""
    # Yeelink device ID
    device_id = 0
    # Sensor number
    sensor['ping'] = 0
    sensor['download'] = 0
    sensor['upload'] = 0
    sensor['lostpercent'] = 0
    sensor['min'] = 0
    sensor['avg'] = 0
    sensor['max'] = 0
    sensor['stddev'] = 0

    # Program behavior settings
    # Fake Speedtest result for debugging.
    fakeSpeedtestResult = 0
    # Fake ping result for debugging.
    # 1 for Debian, 2 for Windows, 3 for OS X.
    fakePingResult = 0
    # Fake yeelink.com post status.
    # 0 to disable. An HTTP response code (e.g. 200) will enable this option.
    fakePostStatus = 0
    # Output detailed debug message.
    verboseMode = 1
    # Log level setting
    # All level < logLevel won't be shown.
    # 0 = info
    # 1 = warning
    # 2 = error
    # 3 = fatal error
    logLevel = 1
    # Output every system command call. Default log level is info(0).
    showCommandOutput = 0
    pingServerName = "itunes.apple.com"
    networkTimeout = 30
    pingTimeout = 180
    speedtestTimeout = 180
