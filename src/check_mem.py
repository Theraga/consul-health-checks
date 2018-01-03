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
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    if mem.percent >= crit or swap.percent >= crit:
        print("MEM CRITICAL: %s%% memory used -- %s%% swap used" % (mem.percent, swap.percent))
        sys.exit(STATE_CRITICAL)
    if mem.percent >= warn or swap.percent >= warn:
        print("MEM WARNING: %s%% memory used -- %s%% swap used" % (mem.percent, swap.percent))
        sys.exit(STATE_WARNING)

    print("MEM OK: %s%% memory used -- %s%% swap used" % (mem.percent, swap.percent))
    sys.exit(STATE_OK)

except Exception as e:
    print(traceback.format_exc())
    sys.exit(STATE_CRITICAL)
