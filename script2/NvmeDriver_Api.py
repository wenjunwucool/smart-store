import requests
import json
from requests.auth import HTTPBasicAuth
import time 
import csv
import sys
IP_ADDR = 'http://10.239.173.71/api/'
SERVER = 'http://10.239.173.71'
username = 'admin'
password = '1'

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
def upload_nvme_driver_from_csvfile():
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    #get_nvme_driver_result_list()
    file_path = sys.argv[3]
    csvfile = file(file_path,'rb')
    reader = csv.reader(csvfile)
    for line in reader:
        print line
        new_nvme_driver_trend_result('',line[7],line[9],line[8],1,create_time,line[3],line[1],line[2],line[0],line[4],60,line[9],line[10],line[11])

    csvfile.close()
