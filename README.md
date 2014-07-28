xifi-mapReducer
===============

##This repo is composed by 3 pairs of scripts:
1. Region (entity) map/reduce scripts:
    a.mapperRegion.py
    b.reducerRegion.py
2. Host service (entity) map/reduce scripts:
    a.mapperHS.py
    b.reducerHS.py
3. VM (entity srcipts)
    a. mapperVM.py
    b. reduucerVM.py

##The final Tables schema will be:
* Table region:

|entityId\* |entityType |aggregationType|timestampId\*|avg_ram_used|avg_ram_tot|avg_core_enabled|avg_core_used|avg_core_tot|avg_hd_used|avg_hd_tot|avg_vm_tot|
|-----------|-----------|---------------|-------------|------------|-----------|----------------|-------------|------------|-----------|-----------|---------|
|varchar(16)|varchar(16)|varchar(8)    |timestamp    |float       |float      |float           |float        |float       |float      |float      |float    |

*with primary keys  (entityId, timestampId)*


* Table vm:

|entityId\* |region\*   |entityType     |aggregationType|timestampId\*|avg_usedMemPct |avg_freeSpacePct|avg_cpuLoadPct|
|-----------|-----------|---------------|---------------|-------------|---------------|----------------|--------------|
|varchar(64)|varchar(16)|varchar(16)    |varchar(8)    |timestamp    |float          |float           |float         |


*with primary keys  (entityId, region, timestampId)*


* Table host_service:

|entityId\* |region\*   |entityType\*     |serviceType\*|aggregationType|timestampId\*|avg_usedMemPct |avg_freeSpacePct|avg_cpuLoadPct|
|-----------|-----------|-----------------|-------------|---------------|-------------|---------------|----------------|--------------|
|varchar(64)|varchar(32)|varchar(32)      |varchar(32)  |varchar(8)     |timestamp    |float          |float           |float         |


*with primary keys (entityId, region, entityType,serviceType,timestampId )*
