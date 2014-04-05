#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

import sys
import datetime
import os
import subprocess
import threading
from config import Config

__all__ = ["logLevelString", "log", "getCurrentTime", "readCommandOutput", "Command"]

try:
    import builtins
except ImportError:
    def print_(*args, **kwargs):
        """The new-style print function taken from
        https://pypi.python.org/pypi/six/

        """
        fp = kwargs.pop("file", sys.stdout)
        if fp is None:
            return

        def write(data):
            if not isinstance(data, basestring):
                data = str(data)
            fp.write(data)

        want_unicode = False
        sep = kwargs.pop("sep", None)
        if sep is not None:
            if isinstance(sep, unicode):
                want_unicode = True
            elif not isinstance(sep, str):
                raise TypeError("sep must be None or a string")
        end = kwargs.pop("end", None)
        if end is not None:
            if isinstance(end, unicode):
                want_unicode = True
            elif not isinstance(end, str):
                raise TypeError("end must be None or a string")
        if kwargs:
            raise TypeError("invalid keyword arguments to print()")
        if not want_unicode:
            for arg in args:
                if isinstance(arg, unicode):
                    want_unicode = True
                    break
        if want_unicode:
            newline = unicode("\n")
            space = unicode(" ")
        else:
            newline = "\n"
            space = " "
        if sep is None:
            sep = space
        if end is None:
            end = newline
        for i, arg in enumerate(args):
            if i:
                write(sep)
            write(arg)
        write(end)
else:
    print_ = getattr(builtins, 'print')
    del builtins

logSerial = 0
logLevelString = {
    0:"Info",
    1:"Warning",
    2:"Error",
    3:"Fatal Error"
    }

def log(context, level = 0, noInfo = False, end = "\n"):
    '''Print out log text when verbose mode enabled.

Log level definition:

0 = info
1 = warning
2 = error
3 = fatal error
'''
    if (Config.verboseMode == 0 or level < Config.logLevel):return 0
    global logSerial
    logSerial = logSerial + 1
    time = getCurrentTime()
    for line in str(context).split("\n"):
        if line == "": print_("\n")
        elif noInfo == True:print_(line, end = end)
        else: print_(logLevelString[level] + "[" + str(logSerial) + ":" + time + "]" + line, end = end)
    return 0

def getCurrentTime():
    '''Return a string for current time.'''
    return str(datetime.datetime.now())

# This is a class for running a command with timeout settings.
# See http://stackoverflow.com/a/4825933 for further information.
# usage:
# command = Command("echo 'Process started'; sleep 2; echo 'Process finished'")
# command.run(timeout=3)
# command.run(timeout=1)
class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            log('Thread started', 0)
            self.process = subprocess.Popen(self.cmd, shell=True)
            self.process.communicate()
            log('Thread finished', 0)

        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            log('Terminating process', 2)
            self.process.terminate()
            thread.join()
        l = 0
        # Dirty hack to make try: block work. Otherwise it raises an AttributeError: 'NoneType' object has no attribute 'returncode'.
        try:
            if self.process.returncode != 0: l = 2
            log("Process finished with exit code: " + str(self.process.returncode), l)
        except:
            log(self.process.returncode)

def __readCommandOutput(command, mtimeout):
    '''Read the output of a command.'''
    if Config.showCommandOutput != 0:
        log("Running command: " + command)
    #result = os.popen(command).read()
    
    if mtimeout < 0:
        result = os.popen(command).read()
    else:
        c = Command(command)
        c.run(timeout = mtimeout)
    if Config.showCommandOutput != 0:
        log("Command output:\n" + result, noInfo = True)
    return result

def readCommandOutput(command, timeout = -1):
    return __readCommandOutput(command, timeout)
