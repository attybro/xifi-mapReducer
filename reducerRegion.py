#!/usr/bin/python
from operator import itemgetter
import sys
import time
import datetime


probe = {}


current_entityId=None
current_count   =0
entityId        =None
myList=[]

##This is the referece time
sysTimestamp=time.time();
actualSample=datetime.date.fromordinal(datetime.date.today().toordinal()-1)
sysDateClean=datetime.datetime(actualSample.year, actualSample.month, actualSample.day,0,0,0)
sysMin=time.mktime(sysDateClean.timetuple())
sysMax=sysMin+(24*60*60)

# input comes from STDIN
for line in sys.stdin:
  base={
  '0': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '1': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '2': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '3': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '4': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '5': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '6': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '7': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '8': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '9': {'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '10':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '11':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '12':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '13':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '14':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '15':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '16':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '17':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '18':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '19':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '20':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '21':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '22':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 },
  '23':{'ramUsed':0, 'CramUsed':0, 'ramTot':0, 'CramTot':0, 'coreUsed':0, 'CcoreUsed':0,'coreEnabled':0, 'CcoreEnabled':0, 'coreTot':0, 'CcoreTot':0, 'hdUsed':0, 'ChdUsed':0, 'hdTot':0, 'ChdTot':0, 'vmUsed':0, 'CvmUsed':0 ,'vmTot':0, 'CvmTot':0 }
  }
  ipAddress = None;
  System_uptime=None;
  present=0;
  line = line.strip()
  #entityId, block = line.split('\t')
  #entityType, agg_name, agg_type, count, timeInterval = block.split('|')
  block, timeInterval = line.split('\t')
  entityId, entityType, agg_name, agg_type, count = block.split('|')

  #if (float(timeInterval)>=sysMin and float(timeInterval)<sysMax):
  try:
    count=int(count)
  except ValueError:
    count=str(count)
  if (probe.get(entityId)):
    tmpDate=datetime.datetime.fromtimestamp(float(timeInterval))
    hour=str(tmpDate.hour)
    if (agg_name=='location' or agg_name=='latitude' or agg_name=='longitude' or agg_name=='timeSample' or agg_name=='_timestamp' or agg_name=='vmImage' or  agg_name=='vmList'):
      continue;
    else:
      probe[entityId][hour][agg_name]+=count
      probe[entityId][hour]['C'+agg_name]+=1
  else:
    tmpDate=datetime.datetime.fromtimestamp(float(timeInterval))
    hour=str(tmpDate.hour)
    if (agg_name=='location' or agg_name=='latitude' or agg_name=='longitude' or agg_name=='timeSample' or agg_name=='_timestamp' or agg_name=='vmImage' or  agg_name=='vmList'):
      continue;
    else:
      probe[entityId]=base;
      probe[entityId][hour][agg_name]+=count
      probe[entityId][hour]['C'+agg_name]+=1



for probeId in probe:
  for timeId in probe.get(probeId):
    #'Test' if 1 == 1 else 'NoTest
    avR_U= 0 if probe.get(probeId).get(timeId).get('CramUsed')== 0  else (float(probe.get(probeId).get(timeId).get('ramUsed'))/float(probe.get(probeId).get(timeId).get('CramUsed')))

    avR_T=0 if probe.get(probeId).get(timeId).get('CramTot')== 0  else float(probe.get(probeId).get(timeId).get('ramTot'))/float(probe.get(probeId).get(timeId).get('CramTot'))

    avC_U=0 if probe.get(probeId).get(timeId).get('CcoreUsed')== 0  else float(probe.get(probeId).get(timeId).get('coreUsed'))/float(probe.get(probeId).get(timeId).get('CcoreUsed'))

    avC_E=0 if probe.get(probeId).get(timeId).get('CcoreEnabled')== 0  else float(probe.get(probeId).get(timeId).get('coreEnabled'))/float(probe.get(probeId).get(timeId).get('CcoreEnabled'))

    avC_T=0 if probe.get(probeId).get(timeId).get('CcoreTot')== 0  else float(probe.get(probeId).get(timeId).get('coreTot'))/float(probe.get(probeId).get(timeId).get('CcoreTot'))

    avH_U=0 if probe.get(probeId).get(timeId).get('ChdUsed')== 0  else float(probe.get(probeId).get(timeId).get('hdUsed'))/float(probe.get(probeId).get(timeId).get('ChdUsed'))

    avH_T=0 if probe.get(probeId).get(timeId).get('ChdTot')== 0  else float(probe.get(probeId).get(timeId).get('hdTot'))/float(probe.get(probeId).get(timeId).get('ChdTot'))

    avV_T=0 if probe.get(probeId).get(timeId).get('CvmTot')== 0  else float(probe.get(probeId).get(timeId).get('vmTot'))/float(probe.get(probeId).get(timeId).get('CvmTot'))

    print '%s\tregion\th\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s'% (probeId, datetime.datetime.fromtimestamp(float(sysMin)+float(timeId)*3600), str(avR_U), str(avR_T), str(avC_U), str(avC_E), str(avC_T), str(avH_U), str(avH_T), str(avV_T) )
