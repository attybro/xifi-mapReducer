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
sysTimestamp=time.time();
#sysTimestamp=1406861999
#sysTimestamp=1406867707
#sysTimestampDelta=sysTimestamp-3600;
#sysDate=datetime.datetime.fromtimestamp(sysTimestampDelta)
actualSample=datetime.date.fromordinal(datetime.date.today().toordinal()-1)
sysDateClean=datetime.datetime(actualSample.year, actualSample.month, actualSample.day,0,0,0)
sysMin=time.mktime(sysDateClean.timetuple())
sysMax=sysMin+(24*60*60)
prova={}
probe = {}

for line in sys.stdin:
  line = line.strip()
  block, timeInterval = line.split('\t')
  _time=int(math.floor( (float(timeInterval)-sysMin)/(60*60) ))
  time_s=str(_time)
  entityId, entityType, agg_name, agg_type, count = block.split('|')
  host_temp=entityId.replace("_"+agg_name, "", len(agg_name))
  regionId=host_temp.split('_')[0]
  hostId=host_temp.replace((regionId)+'_',"")
  #print timeInterval
  plainTimeInterval=datetime.datetime.fromtimestamp(float(timeInterval))
  _time_min=int(math.floor( (float(plainTimeInterval.minute))  /(10.0) ))
  #print plainTimeInterval.minute
  #print _time_min
  
  
  #print (agg_name)
  if int(time_s)>=0:
    if prova.get(agg_name):
      #print agg_name+" "+hostId+" "+str(_time)+" "+str(_time_min)
      if prova.get(agg_name).get(hostId):
        #hs OK node OK
        #print ">>>>>>>>>>hs OK node OK"
        prova.get(agg_name).get(hostId).get(time_s)[str(int(_time_min))]=(int(count))

      else:
        #print ">>>>>>>>>>hs OK node NO"
        prova[agg_name][hostId]={'0':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'1':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'2':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'3':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'4':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'5':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'6':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'7':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'8':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'9':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'10':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'11':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'12':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'13':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'14':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'15':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'16':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'17':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'18':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'19':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'20':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'21':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'22':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'23':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1}}
        prova.get(agg_name).get(hostId).get(time_s)[str(int(_time_min))]=(int(count))

    else:
      if time_s >=0:
        #print ">>>>>>>>>>insert"
        probe[agg_name]={'0':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'1':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'2':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'3':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'4':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'5':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'6':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'7':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'8':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'9':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'10':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'11':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'12':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'13':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'14':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'15':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'16':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'17':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'18':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'19':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'20':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'21':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'22':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'23':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1}};
        prova[agg_name]={hostId:{'0':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'1':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'2':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'3':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'4':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'5':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'6':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'7':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'8':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'9':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'10':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'11':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'12':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'13':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'14':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'15':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'16':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'17':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'18':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'19':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'20':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'21':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'22':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1},'23':{'0':-1, '1':-1,'2':-1,'3':-1,'4':-1,'5':-1}}}
        #print prova.get(agg_name).get(hostId).get(time_s).get('0')
        prova.get(agg_name).get(hostId).get(time_s)[str(int(_time_min))]=(int(count))

        #print prova.get(agg_name)
        #print (time_s)
  else:
    continue;

for _prova1 in prova:
  #print _prova1
  for _prova2 in prova.get(_prova1):
    #print _prova2
    for _prova3 in prova.get(_prova1).get(_prova2):
      #print _prova3
      _len=len (prova.get(_prova1).get(_prova2).get(_prova3))
      #print prova.get(_prova1).get(_prova2).get(_prova3)
      if (_len>0):
        preSample=-1
        for i in range(0,_len):
          sample=prova.get(_prova1).get(_prova2).get(_prova3).get(str(i))
          #if _prova1== 'quantum_metadata_agent' and _prova2 =="node_2" and _prova3=="8":
	    #print str(i)+"  "+str(sample)+"["+str(preSample)+"]"
	  if preSample==-1 and sample==-1:
	    sampleValue=0;
	    preSample=0;
	    #if _prova1== 'quantum_metadata_agent' and _prova2 =="node_2" and _prova3=="8":
	    #  print str(preSample)+"<-->"+str(sampleValue)
	  elif preSample==1 and sample==-1:
	    sampleValue=1
	    preSample=1
	    #if _prova1== 'quantum_metadata_agent' and _prova2 =="node_2" and _prova3=="8":
	    #  print str(preSample)+"<-->"+str(sampleValue)
          elif preSample==0 and sample==-1:
	    sampleValue=0
	    preSample=0
	    #if _prova1== 'quantum_metadata_agent' and _prova2 =="node_2" and _prova3=="8":
	    #  print str(preSample)+"<-->"+str(sampleValue)
	  else:
	    preSample=prova.get(_prova1).get(_prova2).get(_prova3).get(str(i))
	    sampleValue=preSample
	    #if _prova1== 'quantum_metadata_agent' and _prova2 =="node_2" and _prova3=="8":
	    #  print str(preSample)+"<-->"+str(sampleValue)
          prova.get(_prova1).get(_prova2).get(_prova3)[str(i)]=sampleValue

#print prova
#print probe


for _prova1 in prova:
  for _prova2 in prova.get(_prova1):
    for _prova3 in prova.get(_prova1).get(_prova2):
      _len=len (prova.get(_prova1).get(_prova2).get(_prova3))
      if (_len>0):
        for i in range(0,_len):
	  sampleVal=prova.get(_prova1).get(_prova2).get(_prova3).get(str(i))
          probeVal=probe.get(_prova1).get(_prova3).get(str(i))
          #print str(probeVal) +" vs "+str(sampleVal)
	  if(probeVal == -1):
	    probe.get(_prova1).get(_prova3)[str(i)]=sampleVal
	  elif probeVal== 1:
	    continue;
	  elif probeVal==0:
	    probe.get(_prova1).get(_prova3)[str(i)]=sampleVal
	
	    
#print probe
	  

for _probe1 in probe:
  for _probe2 in probe.get(_probe1):
    total=0
    #print _probe2
    for _probe3 in probe.get(_probe1).get(_probe2):
      valS=int(probe.get(_probe1).get(_probe2).get(_probe3))
      #print "  "+str(valS)
      total+=valS
    totCounted=(len(probe.get(_probe1).get(_probe2)))
    av_UP= 0 if totCounted== 0  else (float(total)/float(totCounted))
    print '%s-%s\t%s\thost_service\t%s\th\t%s\t%s' % (regionId,_probe1, regionId,_probe1, datetime.datetime.fromtimestamp(float(sysMin)+float(_probe2)*3600), av_UP  )



