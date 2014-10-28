#!/usr/bin/env python
import sys
import time
import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
    words = line.split()
    # increase counters
    for word in words:
        a1,a2, a3,a4, a5, a6, a7= word.split('|')
        if (a4=="host_compute" and a5!="_timestamp"):
          sampleTime=datetime.datetime.fromtimestamp(int(a2)).strftime('%H')
          print '%s|%s|%s|%s|%s\t%s' % (a3, a4, a5, a6, a7, a2)
        else:
          continue;

