#!/usr/bin/env python
from operator import itemgetter
import sys
import time
import datetime
import math

current_entityId=None
current_count   =0
entityId        =None
myList=[]

##This is the referece time
#sysTimestamp=time.time();
sysTimestamp=1405931644
sysTimestampDelta=sysTimestamp-300;
sysDate=datetime.datetime.fromtimestamp(sysTimestampDelta)
sysDateClean=datetime.datetime(sysDate.year, sysDate.month, sysDate.day,0,0,0)
sysMin=time.mktime(sysDateClean.timetuple())
sysMax=sysMin+(24*60*60)
prova={}
probe = {}

for line in sys.stdin:
  timeArray={'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'11':[],'12':[],'13':[],'14':[],'15':[],'16':[],'17':[],'18':[],'19':[],'20':[],'21':[],'22':[],'23':[]}
  line = line.strip()
  block, timeInterval = line.split('\t')
  _time=int(math.floor( (float(timeInterval)-sysMin)/(60*60) ))
  time_s=str(_time)
  entityId, entityType, agg_name, agg_type, count = block.split('|')
  host_temp=entityId.replace("_"+agg_name, "", len(agg_name))
  regionId=host_temp.split('_')[0]
  hostId=host_temp.replace((regionId)+'_',"")
  if prova.get(agg_name):
    if prova.get(agg_name).get(hostId):
      prova.get(agg_name).get(hostId).get(time_s).append(count)
    else:
      prova.get(agg_name)[hostId]=timeArray
      prova.get(agg_name).get(hostId).get(time_s).append(count)
  else:
    probe[agg_name]=timeArray
    prova[agg_name]={hostId:timeArray}
    prova.get(agg_name).get(hostId).get(time_s).append(count)

for _prova1 in prova:
  for _prova2 in prova.get(_prova1):
    for _prova3 in prova.get(_prova1).get(_prova2):
      _len=len (prova.get(_prova1).get(_prova2).get(_prova3))
      if (_len>0):
        i=0;
        for ii in (prova.get(_prova1).get(_prova2).get(_prova3)):
          if ii=='1':
            probe.get(_prova1).get(_prova3)[i]=ii;
          i=i+1

for _probe1 in probe:
  for _probe2 in probe.get(_probe1):
    total=0
    for _probe3 in probe.get(_probe1).get(_probe2):
      total+=int(_probe3)
    totCounted=(len(probe.get(_probe1).get(_probe2)))
    av_UP= 0 if totCounted== 0  else (float(total)/float(totCounted))
    print '%s-%s\t%s\thost_service\t%s\th\t%s\t%s' % (regionId,_probe1, regionId,_probe1, datetime.datetime.fromtimestamp(float(sysMin)+float(_probe2)*3600), av_UP  )


