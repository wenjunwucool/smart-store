import requests
import json
from requests.auth import HTTPBasicAuth
import time 
IP_ADDR = 'http://10.239.173.54/api/'
SERVER = 'http://10.239.173.54'
username = 'admin'
password = '1'

def get_vhost_scsi_trend_result_list():
    url='{server_add}/api/{project}/vhost_scsi_trend_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()

def new_vhost_scsi_trend_result(result_id,iops,latency,testexecution,create_time,rw_method,queue_depth,io_size):
    url='{server_add}/api/{project}/vhost_scsi_trend_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    payload={'id':result_id,'trend_iops':iops,'trend_latency':latency,'testexecution':testexecution,'create_time':create_time,'rw_method':rw_method,'queue_depth':queue_depth,'io_size':io_size}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        print '###API acsses success ###'
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None

def get_vhost_scsi_perf_result_list():
    url='{server_add}/api/{project}/spdk_perf_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()

#def new_testrecord_list():
def new_vhost_scsi_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    url='{server_add}/api/{project}/spdk_perf_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    payload={'id':result_id,'iops':iops,'latency':latency,'case_type':case_type,'testexecution':testexecution,'create_time':create_time,'rw_method':rw_method,'queue_depth':queue_depth,'io_size':io_size}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        print '###API acsses success ###'
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None


#get_vhost_scsi_trend_result_list()
#new_vhost_scsi_trend_result('',33333,1234,1,"now()",1,1,1)
#get_vhost_scsi_perf_result_list()
