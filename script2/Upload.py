import sys
import re
import os
from functools import wraps
from subprocess import call 
from API1226 import Draw_QueueDepth_Detail_Chart,Draw_Vhost_Scsi_QueueDepth_Detail_Chart
from trend_api import *
from fio_performance_reporter import *
'''
aggrb = ' '
iops_set = {}
lat_set = {}
cpu_usage_set = {}
Total_iops_list=[]
Total_lat_list=[]
'''
if len(sys.argv) < 2: 
    print 'Need argv. you can use --help to show the help cmd'
    sys.exit()
    
if len(sys.argv) > 2: 
    if sys.argv[1].startswith('--'): 
        option = sys.argv[1][2:] 

        if option == 'help': 
            print ''' 
Options include: 
--help  :  Display this help
--vhost :  Upload Vhost test result
--nvmf  :  Upload nvmf-target test result
--nvme  :  Upload the nvme-driver test result
--trend :  Upload the test result to the web 
--detail:  Upload the detail result to the web
--all   :  Upload all result include detail and trend

Example:
    Use cmd: "python Upload.py --nvmf --trend" Upload nvmf-target trend test result
    Use cmd: "python Upload.py --vhost --detail"  Upload vhost detail test result
    Use cmd: "python Upload.py --resultt --path /home/automation_1/DTF/fio_log/2017-06-24/"  Get result from fio log directory.
'''
        else: 
            print "Unknown option: Use --help to get the option help"
        sys.exit() 
if len(sys.argv) > 2:
    if sys.argv[1].startswith('--'): 
        option = sys.argv[1][2:] 
        select = sys.argv[2][2:]
# fetch sys.argv[1] but without the first two characters 
    if option == 'nvmf':
        if select == 'all':
            get_result_from_fio_log()
            Draw_QueueDepth_Detail_Chart(rw_iops,rw_lat)
            print 'nvmf-target all reault upload success!'
        if select == 'trend':
            get_result_from_fio_log()
            upload_trend_result()
            print 'nvmf-target trend result upload success!'
        if select == 'detail':
            print 'nvmf-target detail upload success!'
    if option == 'nvme':
        if select == 'all':
            print 'nvme all'
        if select == 'trend':
            print 'nvme trend'
        if select == 'detail':
            print 'nvme detail'
    if option == 'vhost':
        if select == 'all':
            print 'vhost all'
        if select == 'trend':
            print 'vhost trend'
        if select == 'detail':
            print 'detail detail'
    if option =='result':
        if select == 'file':
            print 'get result from single fil log file'
        if select == 'path':
            get_result_from_fio_log()
            print 'get result from fio log directory path'
    else:
        print "Unknown option: Use --help to get the option help"
                
def trend_api():       
    max_read_iops=max(read_iops)
    max_write_iops=max(write_iops)
    max_rw_iops=max(rw_iops)
    max_randread_iops=max(randread_iops)
    max_randwrite_iops=max(randwrite_iops)
    max_randrw_iops=max(randrw_iops)
    max_read_lat=max(read_lat)
    max_write_lat=max(write_lat)
    max_rw_lat=max(rw_lat)
    max_randread_lat=max(randread_lat)
    max_randwrite_lat=max(randwrite_lat)
    max_randrw_lat=max(randrw_lat)

    def new_spdk_trend_result(result_id,iops,latency,testexecution,create_time,rw_method,queue_depth,io_size):
        url='{server_add}/api/{project}/spdk_trend_result/1/'.format(server_add=SERVER,project='spdk') 
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

    def get_spdk_trend_result_list():
        url='{server_add}/api/{project}/spdk_trend_result/1/'.format(server_add=SERVER,project='spdk') 
        r = requests.get(url, auth=HTTPBasicAuth(username, password))
        r = requests.get(url)
        print r.url
        print r.status_code
        print type(r.json()), r.json()

    def get_rw_id(argv_method):
        if argv_method == "randread":
            rw_method=1
        if argv_method =="write":
            rw_method=2
        if argv_method =="rw":
            rw_method=3
        if argv_method =="read":
            rw_method=4
        if argv_method =="randwrite":
            rw_method=5
        if argv_method =="randrw":
            rw_method==6
        return rw_method

    def draw_spdk_nvmf_target_trend_result():
        create_time=time.strftime('%Y-%m-%d %x',time.localtime())
        new_spdk_trend_result('',max_randread_iops,max_randread_lat,1,create_time,1,1,1)
        #new_spdk_trend_result('',max_read_iops,max_read_lat,1,create_time,1,1,1)
        new_spdk_trend_result('',max_write_iops,max_write_lat,1,create_time,2,1,1)
        new_spdk_trend_result('',max_rw_iops,max_rw_lat,1,create_time,3,1,1)
        #new_spdk_trend_result('',max_randread_iops,max_randread_lat,1,create_time,4,1,1)
        new_spdk_trend_result('',max_read_iops,max_read_lat,1,create_time,4,1,1)
        new_spdk_trend_result('',max_randwrite_iops,max_randwrite_lat,1,create_time,5,1,1)
        new_spdk_trend_result('',max_randrw_iops,max_randrw_lat,1,create_time,6,1,1)

    def draw_vhost_scsi_trend_result():
        create_time=time.strftime('%Y-%m-%d %x',time.localtime())
        new_vhost_scsi_trend_result('',max_randread_iops,max_randread_lat,1,create_time,1,1,1)
        #new_vhost_scsi_trend_result('',max_read_iops,max_read_lat,1,create_time,1,1,1)
        new_vhost_scsi_trend_result('',max_write_iops,max_write_lat,1,create_time,2,1,1)
        new_vhost_scsi_trend_result('',max_rw_iops,max_rw_lat,1,create_time,3,1,1)
        #new_vhost_scsi_trend_result('',max_randread_iops,max_randread_lat,1,create_time,4,1,1)
        new_vhost_scsi_trend_result('',max_read_iops,max_read_lat,1,create_time,4,1,1)
        new_vhost_scsi_trend_result('',max_randwrite_iops,max_randwrite_lat,1,create_time,5,1,1)
        new_vhost_scsi_trend_result('',max_randrw_iops,max_randrw_lat,1,create_time,6,1,1)


    def upload_trend_result():
        create_time=time.strftime('%Y-%m-%d %x',time.localtime())
        print 'max_read_iops',max_read_iops
        print 'max_write_iops',max_write_iops
        print 'max_rw_iops',max_rw_iops
        print 'max_randread_iops',max_randread_iops
        print 'max_randwrite_iops',max_randwrite_iops
        print 'max_randrw_iops',max_randrw_iops
        draw_spdk_nvmf_target_trend_result()
        #draw_vhost_scsi_trend_result()
        #new_vhost_scsi_trend_result('',8888,6666,1,create_time,1,1,1)
