xifi-mapReducer
===============
##General Information
###This repo is composed by 4 pairs of scripts:
1. Region (entity) map/reduce scripts:
    * mapperRegion.py
    * reducerRegion.py
2. Host service (entity) map/reduce scripts:
    * mapperHS.py
    * reducerHS.py
3. VM (entity) srcipts:
    * mapperVM.py
    * reducerVM.py
4. Host script
    * mapperH.py
    * reducerH.py


###The final Table schemas will be:
* Table region:

|entityId\* |entityType |aggregationType|timestampId\*|avg_ram_used|avg_ram_tot|avg_core_enabled|avg_core_used|avg_core_tot|avg_hd_used|avg_hd_tot|avg_vm_tot|
|-----------|-----------|---------------|-------------|------------|-----------|----------------|-------------|------------|-----------|-----------|---------|
|varchar(16)|varchar(16)|varchar(8)    |timestamp    |float       |float      |float           |float        |float       |float      |float      |float    |

*with primary keys  (entityId, timestampId)*


* Table vm:

|entityId\* |region\*   |entityType     |aggregationType|timestampId\*|avg_usedMemPct |avg_freeSpacePct|avg_cpuLoadPct|availability|
|-----------|-----------|---------------|---------------|-------------|---------------|----------------|--------------|------------|
|varchar(64)|varchar(16)|varchar(16)    |varchar(8)    |timestamp    |float          |float           |float          |float       |


*with primary keys  (entityId, region, timestampId)*


* Table host_service:

|entityId\* |region\*   |entityType\*     |serviceType\*|aggregationType|timestampId\*|avg_usedMemPct |avg_freeSpacePct|avg_cpuLoadPct|
|-----------|-----------|-----------------|-------------|---------------|-------------|---------------|----------------|--------------|
|varchar(64)|varchar(32)|varchar(32)      |varchar(32)  |varchar(8)     |timestamp    |float          |float           |float         |


*with primary keys (entityId, region, entityType,serviceType,timestampId )*


* Table host:

|entityId\* |region\*   |hostname   |role     |aggregationType|timestampId\*|avg_usedMemPct |avg_freeSpacePct |avg_cpuLoadPct |host_id  |sysUptime  |
|-----------|-----------|-----------|-----------|----------------|---------------|-------------|---------------|----------------|--------------|------------|
|varchar(64)|varchar(16)|varchar(16)|varchar(16)    |varchar(8)     |timestamp    |float          |float           |float         |varchar(16)    |float       |


*with primary keys  (entityId, region, timestampId)*



##Contact

For any question, bug report, suggestion or feedback in general, please contact me: Attilio Broglio (abroglio at create-net dot org).
