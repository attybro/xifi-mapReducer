#!/usr/bin/python
import sys
import time
import datetime

# input comes from STDIN (standard input)
for line in sys.stdin:
    sanities = line.split()
    for sanity in sanities:
        tmp_array =[]
        tmp_array=sanity.split('|')
        if (len(tmp_array)==7):
	  if(tmp_array[3]=="region" and tmp_array[4].find("sanity")!=-1):
            print '%s|%s|%s|%s|%s\t%s' % (tmp_array[2], tmp_array[3], tmp_array[4], tmp_array[5], tmp_array[6], tmp_array[1])
          else:
	    continue
        else:
          continue;