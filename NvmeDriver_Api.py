import requests
import json
from requests.auth import HTTPBasicAuth
import time 
IP_ADDR = 'http://10.239.173.54/api/'
SERVER = 'http://10.239.173.54'
username = 'admin'
password = '1'

import csv

def get_nvme_driver_result_list():
    url='{server_add}/api/{project}/nvme_driver_trend_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.status_code
    print type(r.json()), r.json()


#def new_nvme_driver_trend_result(result_id,iops,latency,MBps,testexecution,create_time,rw_method,queue_depth,workload_mix,Core_Mask,run_time,Average_lat,Min_lat,Max_lat,io_size):
def new_nvme_driver_trend_result(result_id,iops,latency,MBps,testexecution,create_time,rw_method,queue_depth,workload_mix,io_size,Core_Mask,run_time,Average_lat,Min_lat,Max_lat):
    url='{server_add}/api/{project}/nvme_driver_trend_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #payload={'id':result_id,'trend_iops':iops,'trend_latency':latency,'MBps':MBps,'testexecution':testexecution,'create_time':create_time,'rw_method':rw_method,'queue_depth':queue_depth,'workload_mix':workload_mix,'Core_Mask':Core_Mask,'run_time':run_time,'Average_lat':Average_lat,'Min_lat':Min_lat,'io_size':io_size}
    payload={'id':result_id,'trend_iops':iops,'trend_latency':latency,'MBps':MBps,'testexecution':testexecution,'create_time':create_time,'rw_method':rw_method,'queue_depth':queue_depth,'workload_mix':workload_mix,'io_size':io_size,'Core_Mask':Core_Mask,'run_time':run_time,'Average_lat':Average_lat,'Min_lat':Min_lat,'Max_lat':Max_lat}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r
    print r.url
    print r.json()
    if 201 == r.status_code:
        print '###API acsses success ###'
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None

create_time=time.strftime('%Y-%m-%d %x',time.localtime())
get_nvme_driver_result_list()
#new_nvme_driver_trend_result('',222,111,1,1,create_time,1,1,30,'','',1,1,1,1); 
#new_nvme_driver_trend_result(result_id,iops,latency,MBps,testexecution,create_time,rw_method,queue_depth,workload_mix,io_size,Core_Mask,run_time,Average_lat,Min_lat,Max_lat):
csvfile = file('perf_output.csv','rb')
reader = csv.reader(csvfile)
for line in reader:
    print line
    #new_nvme_driver_trend_result('',line[7],line[9],line[8],1,create_time,6,1,50,line[2],'0x1',1,line[9],line[10],line[11])
    # new_nvme_driver_trend_result(result_id,iops,latency,MBps,testexecution,create_time,rw_method,queue_depth,workload_mix,io_size,Core_Mask,run_time,Average_lat,Min_lat,Max_lat):
    new_nvme_driver_trend_result('',line[7],line[9],line[8],1,create_time,6,1,line[2],1,'0x1',1,line[9],line[10],line[11])

csvfile.close()
