#!/usr/bin/python
from operator import itemgetter
import sys
import time
import datetime
import math

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

sanityRegion=[]


def findElement(regionList, regionId):
  for reg in regionList:
    if (reg['regionID']==regionId):
      return True;
  return False;


# input comes from STDIN
for line in sys.stdin:
  line = line.strip()
  tmp_array_1 =[]
  tmp_array_1 = line.split('\t')
  if (len(tmp_array_1)==2):
    probe_val    = 0;
    block        = tmp_array_1[0]
    timeInterval = tmp_array_1[1]
    _time=int(math.floor( (float(timeInterval)-sysMin)/(60*60) ))
    time_s=str(_time)
    tmp_array_2 =[]
    tmp_array_2 = block.split('|')
    if (len(tmp_array_2)==5):
      regionId   = tmp_array_2[0]
      entityType = tmp_array_2[1]
      probe_id   = tmp_array_2[2]
      date       = tmp_array_2[3]
      value      = tmp_array_2[4]
      if (value=="OK"): probe_val=1
      elif (value=="POK"): probe_val=0.75
      elif (value=="NOK"): probe_val=0
      #start the initailizzation of the Array aboute the regions
      if (len(sanityRegion)==0 or not(findElement(sanityRegion, regionId))):
	#empty list
        sanityRegion.append({"regionID":regionId , 'hour' : {'0':{"sumProbes":0, "countProbes": 0}, '1':{"sumProbes":0, "countProbes": 0},'2':{"sumProbes":0, "countProbes": 0},'3':{"sumProbes":0, "countProbes": 0},'4':{"sumProbes":0, "countProbes": 0},'5':{"sumProbes":0, "countProbes": 0},'6':{"sumProbes":0, "countProbes": 0},'7':{"sumProbes":0, "countProbes": 0},'8':{"sumProbes":0, "countProbes": 0},'9':{"sumProbes":0, "countProbes": 0},'10':{"sumProbes":0, "countProbes": 0},'11':{"sumProbes":0, "countProbes": 0},'12':{"sumProbes":0, "countProbes": 0},'13':{"sumProbes":0, "countProbes": 0},'14':{"sumProbes":0, "countProbes": 0},'15':{"sumProbes":0, "countProbes": 0},'16':{"sumProbes":0, "countProbes": 0},'17':{"sumProbes":0, "countProbes": 0},'18':{"sumProbes":0, "countProbes": 0},'19':{"sumProbes":0, "countProbes": 0},'20':{"sumProbes":0, "countProbes": 0},'21':{"sumProbes":0, "countProbes": 0},'22':{"sumProbes":0, "countProbes": 0},'23':{"sumProbes":0, "countProbes": 0}}})
        sanityRegion[0]['hour'][time_s]['sumProbes']=probe_val
        sanityRegion[0]['hour'][time_s]['countProbes']=1

      elif((len(sanityRegion)>0) and findElement(sanityRegion, regionId)):
        #region already in list
        for r in sanityRegion:
          if (r['regionID']==regionId):
            r['hour'][time_s]['sumProbes']+=probe_val
            r['hour'][time_s]['countProbes']+=1


for regionElement in sanityRegion:
  for tmp_reg  in regionElement['hour']:
    IDreg=regionElement['regionID']
    average=0.0
    if(regionElement['hour'] [tmp_reg]['countProbes']==0):
      average=0.0
    else:
      average=float(regionElement['hour'] [tmp_reg]['sumProbes'])/float(regionElement['hour'] [tmp_reg]['countProbes'])
      
    print '%s-sanity\t%s\thost_service\tsanity\th\t%s\t%s' % (IDreg, IDreg , datetime.datetime.fromtimestamp(float(sysMin)+float(tmp_reg)*3600), average  )

