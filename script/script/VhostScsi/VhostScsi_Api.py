import requests
import json
from requests.auth import HTTPBasicAuth
#from requests.auth import HTTPBasicAuth
#from fio_performance_reporter import * 
import time 
#from upload_rw_method import *
IP_ADDR = 'http://10.239.173.71/api/'
SERVER = 'http://10.239.173.71'
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
    url='{server_add}/api/{project}/vhost_scsi_perf_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()


#def new_testrecord_list():
def new_vhost_scsi_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    url='{server_add}/api/{project}/vhost_scsi_perf_result/1/'.format(server_add=SERVER,project='spdk') 
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
    
def Draw_Vhost_Scsi_QueueDepth_Detail_Chart(rw_iops,rw_lat):

    print "randrw",randrw_iops
    os_id=0
    while os_id<1:
        write_all_rw_method()
        os_id +=1
    return 0
def Draw_Vhost_Scssi_Trend_Chart():
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    i=0;
    while i < 6:
        new_vhost_scsi_trend_result('',80000,1234,1,create_time,5,1,1)
        #print depth_iops_list,depth_lat_list   
Draw_Vhost_Scssi_Trend_Chart()
#get_vhost_scsi_trend_result_list()
#new_vhost_scsi_trend_result('',33333,1234,1,"now()",1,1,1)
#get_vhost_scsi_perf_result_list()
#new_vhost_scsi_perf_result('',33333,1234,1,1,"now()",1,1,1)

