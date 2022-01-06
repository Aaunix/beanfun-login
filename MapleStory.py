import os
import sys

import psutil

lnk = "MapleStory.lnk"
programName = "MapleStory.exe"
start = "start"
space = " "
try:
    for proc in psutil.process_iter():
        if proc.name() == programName:
            prams = psutil.Process(proc.pid).cmdline()
            os.system(start + space + lnk +
                      space + prams[1] +
                      space + prams[2] +
                      space + prams[3] +
                      space + prams[4] +
                      space + prams[5])
            sys.exit()

except Exception as e:
    with open("error.log", 'w') as f:
        f.write(str(e))
    sys.exit()
