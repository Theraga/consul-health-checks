# -*- coding: utf-8 -*-
"""
:project: consul-health-checks
:author: Mick Schellekens (mick.schellekens@axians.com)
:date: 2018-01-03
"""
import psutil
import sys
import traceback

STATE_OK = 0
STATE_WARNING = 1
STATE_CRITICAL = 2
STATE_UNKNOWN = 3
try:
    warn = int(sys.argv[1])
    crit = int(sys.argv[2])

    # This is a status check for disk
    path = sys.argv[3]
    disk = psutil.disk_usage(path)
    if disk.percent >= crit:
        print("DISK CRITICAL: %s%% used" % disk.percent)
        sys.exit(STATE_CRITICAL)
    if disk.percent >= warn:
        print("DISK WARNING: %s%% used" % disk.percent)
        sys.exit(STATE_CRITICAL)

    print("DISK OK: %s%% used" % disk.percent)
    sys.exit(STATE_OK)

except Exception as e:
    print(traceback.format_exc())
    sys.exit(STATE_CRITICAL)
