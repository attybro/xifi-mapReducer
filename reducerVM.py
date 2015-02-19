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
  '0': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '1': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '2': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '3': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '4': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '5': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '6': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '7': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '8': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '9': {'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '10':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '11':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '12':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '13':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '14':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '15':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '16':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '17':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '18':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '19':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '20':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '21':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '22':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0},
  '23':{'usedMemPct':0.0, 'CusedMemPct':0.0, 'freeSpacePct':0.0, 'CfreeSpacePct':0.0, 'cpuLoadPct':0.0, 'CcpuLoadPct':0.0,'host_name':None,'Chost_name':0.0}
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
    count=float(count)
  except ValueError:
    count=str(count)
  if (probe.get(entityId)):
    tmpDate=datetime.datetime.fromtimestamp(float(timeInterval))
    hour=str(tmpDate.hour)
    if (agg_name=='usedMemPct' or agg_name=='freeSpacePct' or agg_name=='cpuLoadPct'):
      probe[entityId][hour][agg_name]+=count
      probe[entityId][hour]['C'+agg_name]+=1
    elif (agg_name=='host_name'):
      probe[entityId][hour][agg_name]=count
      probe[entityId][hour]['C'+agg_name]+=1
    else:
      continue;
  else:
    probe[entityId]=base;
    tmpDate=datetime.datetime.fromtimestamp(float(timeInterval))
    hour=str(tmpDate.hour)
    if (agg_name=='usedMemPct' or agg_name=='freeSpacePct' or agg_name=='cpuLoadPct'):
      probe[entityId][hour][agg_name]+=float(count)
      probe[entityId][hour]['C'+agg_name]+=1
    elif (agg_name=='host_name'):
      probe[entityId][hour][agg_name]=count
      probe[entityId][hour]['C'+agg_name]+=1
    else:
      continue;


for probeId in probe:
  for timeId in probe.get(probeId):
    #print probe.get(probeId)
    #'Test' if 1 == 1 else 'NoTest
    sysUP=0.0
    av_UM= 0 if probe.get(probeId).get(timeId).get('CusedMemPct')== 0  else (float(probe.get(probeId).get(timeId).get('usedMemPct'))/float(probe.get(probeId).get(timeId).get('CusedMemPct')))

    av_FS=0 if probe.get(probeId).get(timeId).get('CfreeSpacePct')== 0  else float(probe.get(probeId).get(timeId).get('freeSpacePct'))/float(probe.get(probeId).get(timeId).get('CfreeSpacePct'))

    av_CL=0 if probe.get(probeId).get(timeId).get('CcpuLoadPct')== 0  else float(probe.get(probeId).get(timeId).get('cpuLoadPct'))/float(probe.get(probeId).get(timeId).get('CcpuLoadPct'))
    
    if (probe.get(probeId).get(timeId).get('Chost_name')== 0):
      sysUP=0.0;
    else:
      sysUP=probe.get(probeId).get(timeId).get('Chost_name')/54
      if (sysUP>1):
        sysUP=1;
     

    print '%s\t%s\tvm\th\t%s\t%s\t%s\t%s\t%s\t%s'% (probeId, (probeId.split('_'))[0], datetime.datetime.fromtimestamp(float(sysMin)+float(timeId)*3600), str(av_UM), str(av_FS), str(av_CL),probe.get(probeId).get(timeId).get('host_name'),str(sysUP) );

