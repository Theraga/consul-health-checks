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

# This is a cpu check for a service
try:
    warn = int(sys.argv[1])
    crit = int(sys.argv[2])
    cpu_p = psutil.cpu_percent(interval=5)
    if cpu_p >= crit:
        print("CPU CRITICAL: %s%%" % cpu_p)
        sys.exit(STATE_CRITICAL)
    if cpu_p >= warn:
        print("CPU WARNING: %s%%" % cpu_p)
        sys.exit(STATE_WARNING)

    print("CPU OK: %s%%" % cpu_p)
    sys.exit(STATE_OK)

except Exception as e:
    print(traceback.format_exc())
    sys.exit(STATE_CRITICAL)
