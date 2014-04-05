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

# all things that can be imported
__all__ = [
    "logLevelString",
    "logLevel",
    "log",
    "getCurrentTime",
    "readCommandOutput",
    "Command"
    ]

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
    0:"Debug",
    1:"Info",
    2:"Warning",
    3:"Error",
    4:"Fatal Error"
    }

class logLevel(object):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    FATALERROR = 4

def log(context, level = 0, noInfo = False, end = "\n"):
    '''Print out log text when verbose mode enabled.

Log level definition:

0 = debug
1 = info
2 = warning
3 = error
4 = fatal error

use logLevel consts.
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
        self.commandOutput = ""
        self.ret = 0

    def run(self, timeout = -1):
        def target():
            log('Thread started', logLevel.DEBUG)
            self.process = subprocess.Popen(self.cmd, shell = True, stdout = subprocess.PIPE)
            self.commandOutput = self.process.stdout.read()
            self.ret = self.process.returncode
            log('Thread finished', logLevel.DEBUG)

        thread = threading.Thread(target = target)
        thread.start()
        if timeout >=0:
            thread.join(timeout)
            if thread.isAlive():
                log('Process timeout. Terminating process...', logLevel.ERROR)
                self.process.terminate()
                thread.join()
        else:
            thread.join()
            
        # Dirty hack to make try: block work. Otherwise it raises an AttributeError: 'NoneType' object has no attribute 'returncode'.
        try:
            if self.ret == 0:
                log("Process finished with exit code " + str(self.process.returncode), logLevel.DEBUG)
            elif self.ret < 0:
                log("Process terminated with signal " + str(-self.process.returncode), logLevel.ERROR)
            else:
                log("Process finished with exit code " + str(self.process.returncode), logLevel.ERROR)
        except:
            log("Return code: " + str(self.ret), 0)

        return self.commandOutput

def __readCommandOutput(command, mtimeout):
    '''Read the output of a command.'''
    if Config.showCommandOutput != 0:
        log("Running command: " + command)
    #result = os.popen(command).read()
    c = Command(command)
    if mtimeout < 0:
        result = c.run()
    else:
        result = c.run(timeout = mtimeout)
    if Config.showCommandOutput != 0:
        log("Command output:\n" + result, logLevel.DEBUG, noInfo = True)
    return result

def readCommandOutput(command, timeout = -1):
    return __readCommandOutput(command, timeout)

if __name__ == '__main__':
    # debug only
    a = Command("echo 1;sleep 2;echo 2")
    b = a.run()
    print b
