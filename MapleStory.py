import os
import sys

import psutil

lnk = "MapleStory.lnk"
programName = "MapleStory.exe"
try:
    for proc in psutil.process_iter():
        if proc.name() == programName:
            prams = psutil.Process(proc.pid).cmdline()
            # 添加启动参数
            os.system("start {} {} {} {} {} {}".format(lnk, prams[1], prams[2], prams[3], prams[4], prams[5]))
            sys.exit()

except Exception as e:
    with open("error.log", 'w') as f:
        f.write(str(e))
    sys.exit()
