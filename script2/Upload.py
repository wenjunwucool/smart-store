import sys
import re
import os
from functools import wraps
from subprocess import call 
from API1226 import *
from trend_api import *
from fio_performance_reporter import *
from NvmeDriver_Api import *
global read_iops,write_iops,rw_iops,randread_iops,randwrite_iops,randrw_iops
global read_lat,write_lat,rw_lat,randread_lat,randwrite_lat,randrw_lat

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
    
if len(sys.argv) >= 2: 
    if sys.argv[1].startswith('--'): 
        option = sys.argv[1][2:] 
        if option == 'help': 
            print ''' 
Options include: 
--help  :  Display this help
--vhost :  Upload Vhost test result
--nvmf  :  Upload nvmf-target test result
--nvme  :  Upload the nvme-driver test result to the web
--trend :  Upload the test result to the web 
--detail:  Upload the detail result to the web
--all   :  Upload all result include detail and trend
--result:  get

Example:
    Use cmd: "python Upload.py --nvmf --trend" Upload nvmf-target trend test result
    Use cmd: "python Upload.py --vhost --detail"  Upload vhost detail test result
    Use cmd: "python Upload.py --result --path /home/automation_1/DTF/fio_log/2017-06-24/"  Get result from fio log directory.
'''
       # else: 
       #     print "Unknown option: Use --help to get the option help1"
       # sys.exit() 
    if len(sys.argv) >2:
    #if sys.argv[1].startswith('--'): 
        #option = sys.argv[1][2:] 
        select = sys.argv[2][2:]
        #print sys.argv[1][2:]
        #print sys.argv[2][2:]
# fetch sys.argv[1] but without the first two characters 
        if option == 'nvmf':
            if select == 'all':
                get_result_from_fio_log()
                draw_spdk_nvmf_target_trend_result()
                Draw_Spdk_QueueDepth_Detail_Chart()
                print 'nvmf-target all reault upload success!'
            if select == 'trend':
                get_result_from_fio_log()
                draw_spdk_nvmf_target_trend_result()
                print 'nvmf-target trend result upload success!'
            if select == 'detail':
                get_result_from_fio_log()
                Draw_Spdk_QueueDepth_Detail_Chart()
                print 'nvmf-target detail upload success!'
        if option == 'nvme':
            if select == 'file':
                upload_nvme_driver_from_csvfile()
                print 'nvme trend'
        if option == 'vhost':
            if select == 'all':
                print 'vhost all'
            if select == 'trend':
                draw_vhost_scsi_trend_result()
                print 'vhost trend'
            if select == 'detail':
                Draw_Vhost_Scsi_QueueDepth_Detail_Chart()
                print 'detail detail'
        if option =='result':
            if select == 'file':
                get_result_from_single_log_file()
                print 'get result from single fil log file'
            if select == 'path':
                print 'get result from fio log directory path'
                get_result_from_fio_log()
                print 'get result from fio log directory path'
        else:
            print "Unknown option: Use --help to get the option help2"
                
