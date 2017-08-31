# -*- coding: utf-8 -*- 
import requests
import json
from requests.auth import HTTPBasicAuth
from fio_performance_reporter import *
import time
from upload_rw_method import *
IP_ADDR = 'http://10.239.173.71/api/'
SERVER = 'http://10.239.173.71'
username = 'admin'
password = '1'

def get_project_list():
    url = IP_ADDR + 'project'
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()


def new_project(project_name):

    url = IP_ADDR + 'project/'
    payload = {'name': project_name}
    r = requests.post(url, payload)
    print r.url
    print r.status_code


def get_testplan_list():
    url = IP_ADDR + 'spdk/testplan'
    #r = requests.get(url)
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.status_code
    print r.json()
    plan_id_list=r.json()
    print '======================\n'
    plan_id=plan_id_list[-1]['id']
    print "^^^^^^^^^^^^^^^^^^^^^",plan_id
    #print plan_id_list[-1]
    print '======================\n'
    return plan_id


def get_testexecution_list():
    url ='{server_add}/api/{project}/testexecution/'.format(server_add=SERVER,project='spdk')
    #r = requests.get(url)
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.status_code
    #print r.json()
    exe_id_list=r.json()
    exe_id=exe_id_list[-1]['id']
    print '===================='
    print exe_id
    print '===================='
    return exe_id

def new_dpdk_testplan(plan_id,plan_name,rw_method_id,io_size_id,queue_size_id,owner,create_time,description,del_flag):
#def new_dpdk_testplan():
    url = '{server_add}/api/{project}/testplan/'.format(server_add=SERVER,project='spdk') 
    payload={'id':plan_id,'name':plan_name,'queue_depth':queue_size_id,'rw':rw_method_id,'io_size':io_size_id,'owner':owner,'create_time':create_time,'description':description,'del_flag':del_flag}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None


def new_dpdk_testresult(result_id,exe_id,suit_id,zero_loss_throughput,zero_loss_rate,create_time):
#def new_dpdk_testresult():
    url = '{server_add}/api/dpdk/myresult/1/'.format(server_add=SERVER,project='dpdk') 
    #payload={'id':2 ,'name':"dpdk2",'category':1,'performance':True,'app':1,'owner':"admin",'create_time':"2016-10-24T17:39:17Z",'start_time':"2016-10-24T17:39:17Z",'end_time':"2016-10-24T17:39:17Z",'description':"null"}
    #payload={'id':1,'testexecution':2,'testsuite':1,'passed':12,'failed':21,'block':1,'na':1,'total':14}#'time':"2016-10-24T17:39:17Z",}
    payload={'id':result_id,'testexecution':exe_id,'testsuite':suit_id,'zero_loss_throughput':zero_loss_throughput,'zero_loss_rate':zero_loss_rate,'time':"create_time"}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None


def update_dpdk_testresult(result_id,exe_id,suit_id,zero_loss_throughput,zero_loss_rate,create_time):
#def new_dpdk_testresult():
    url ='{server_add}/api/{project}/myresult/{id}/'.format(server_add=SERVER,project='dpdk',id=suit_id) 
    #payload={'id':2 ,'name':"dpdk2",'category':1,'performance':True,'app':1,'owner':"admin",'create_time':"2016-10-24T17:39:17Z",'start_time':"2016-10-24T17:39:17Z",'end_time':"2016-10-24T17:39:17Z",'description':"null"}
    #payload={'id':1,'testexecution':2,'testsuite':1,'passed':12,'failed':21,'block':1,'na':1,'total':14}#'time':"2016-10-24T17:39:17Z",}
    payload={'id':result_id,'testexecution':exe_id,'testsuite':suit_id,'zero_loss_throughput':zero_loss_throughput,'zero_loss_rate':zero_loss_rate,'time':"create_time"}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None


def create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    url = '{server_add}/api/{project}/testexecution/'.format(server_add=SERVER,project='dpdk')
    payload = {'name': name, 'rw': rw, 'io_size': io_size, 'queue_depth': queue_depth,
               'runner': runner, 'time': create_time, 'testplan': testplan, 'environment': environment}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None

#####get方法######
def update_execution(plan_id, name, os, platform, runner, project, performance, app):
    url = '{server_add}/api/{project}/testexecution/'.format(server_add=SERVER,
            project='dpdk')
    payload = {'name': name, 'os': os, 'platform': platform, 'testplan': plan_id,
               'runner': runner, 'project': project, 'performance': performance, 'app': app}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None

####################### dpdk testrecord ##############################
def get_testrecord_list():
    url ='{server_add}/api/{project}/testrecord/1/'.format(server_add=SERVER,project='dpdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()

#def new_testrecord_list():
def new_testrecord_list(result_id,case_name,case_type,create_time,branch_commit_id,commit_info,test_command,board_name,cpu_info,memory_info,nic_name,device,firmware,distro_info,kernel_info,gcc_info):
    url ='{server_add}/api/{project}/testrecord/1/'.format(server_add=SERVER,project='dpdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    payload={'id':result_id,'case_name':case_name,'case_type':case_type,'create_time':create_time,'branch_commit_id':branch_commit_id,'commit_info':commit_info,'test_command':test_command,'board_name':board_name,'cpu_info':cpu_info,'memory_info':memory_info,'nic_name':nic_name,'device':device,'firmware':firmware,'distro_info':distro_info,'kernel_info':kernel_info,'gcc_info':gcc_info}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None
######################################################################

####################### spdk testrecord ##############################
def get_spdk_perf_result_list():
    url='{server_add}/api/{project}/spdk_perf_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()

#def new_testrecord_list():
def new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
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
### 0106 #######    
def new_spdk_trend_result(result_id,iops,latency,testexecution,create_time,rw_method,queue_depth,io_size):
    url='{server_add}/api/{project}/spdk_trend_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    payload={'id':result_id,'iops':iops,'latency':latency,'testexecution':testexecution,'create_time':create_time,'rw_method':rw_method,'queue_depth':queue_depth,'io_size':io_size}
    r = requests.post(url, payload, auth=HTTPBasicAuth(username, password))
    print r.url
    print r.json()
    if 201 == r.status_code:
        print '###API acsses success ###'
        execution = json.loads(r.text)
        return execution['id']
    else:
        return None

def Draw_QueueDepth_Chart():
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    count=0
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    #print create_time
    new_dpdk_testplan('',"Fio_TestResult20",1,True,1,'admin',"create_time","2016-10-30T10:00:53Z","2016-10-30T10:00:53Z","Fio_TestResult")
    #print float(iops_data_list[count])
    while count<1:
        create_execution(plan_id+1,"1_Queue_depth",3,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[count]),float(lat_data_list[count]),"fio_test",exe_id+1,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"2_Queue_depth",3,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[count+1]),float(lat_data_list[count+1]),"fio_test",exe_id+2,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"4_Queue_depth",3,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[count+2]),float(lat_data_list[count+2]),"fio_test",exe_id+3,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"8_Queue_depth",3,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[count+3]),float(lat_data_list[count+3]),"fio_test",exe_id+4,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"16_Queue_depth",3,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[count+4]),float(lat_data_list[count+4]),"fio_test",exe_id+5,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"32_Queue_depth",3,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[count+5]),float(lat_data_list[count+5]),"fio_test",exe_id+6,'2016-10-30T10:00:53Z')

        count+=1
    return 0
################################################    
def Draw_QueueDepth_Os_Chart():
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    os_id=1
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    #print create_time
    new_dpdk_testplan('',"Fio_TestResult20",1,True,1,'admin',"create_time","2016-10-30T10:00:53Z","2016-10-30T10:00:53Z","Fio_TestResult")
    #print float(iops_data_list[0])
    while os_id<5:
        create_execution(plan_id+1,"1_Queue_depth",os_id,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"fio_test",exe_id+1,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"2_Queue_depth",os_id,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[1]),float(lat_data_list[1]),"fio_test",exe_id+2,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"4_Queue_depth",os_id,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[2]),float(lat_data_list[2]),"fio_test",exe_id+3,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"8_Queue_depth",os_id,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[3]),float(lat_data_list[3]),"fio_test",exe_id+4,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"16_Queue_depth",os_id,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[4]),float(lat_data_list[4]),"fio_test",exe_id+5,'2016-10-30T10:00:53Z')

        create_execution(plan_id+1,"32_Queue_depth",os_id,1,"admin",2,True,1)
        new_spdk_perf_result('',float(iops_data_list[5]),float(lat_data_list[5]),"fio_test",exe_id+6,'2016-10-30T10:00:53Z')
        exe_id +=6

        os_id +=1
        if os_id==2:
            os_id +=1
        else:
            pass
    return 0


#####################################################
def Draw_QueueDepth_Detail_Chart(rw_iops,rw_lat):
    print "randrw",randrw_iops
    #plan_id = get_testplan_list()
    #plan_id = 9
    #exe_id = get_testexecution_list()
    os_id=0
    #create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    #print create_time
    #new_dpdk_testplan('','nvmf-target',2,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    #print float(iops_data_list[0])
    while os_id<1:

        draw_randrw_chart(rw_iops,rw_lat)
        draw_randwrite_chart(randwrite_iops,randwrite_lat)
        draw_randread_chart(randread_iops,randread_lat)
        draw_read_chart(read_iops,read_lat)
        draw_write_chart(write_iops,write_lat)
        draw_rw_chart(rw_iops,rw_lat)
        #exe_id +=6
        os_id +=1
        #if os_id==2:
        #    os_id +=1
        #else:
        #    pass
    return 0

def Draw_Vhost_Scsi_QueueDepth_Detail_Chart(rw_iops,rw_lat):
    #print "randrw",randrw_iops
    os_id=0
    while os_id<1:
        draw_randrw_chart(rw_iops,rw_lat)
        draw_randwrite_chart(randwrite_iops,randwrite_lat)
        draw_randread_chart(randread_iops,randread_lat)
        draw_read_chart(read_iops,read_lat)
        draw_write_chart(write_iops,write_lat)
        draw_rw_chart(rw_iops,rw_lat)
        os_id +=1
    return 0

def Draw_Trend_Chart():
#def new_spdk_trend_result(result_id,iops,latency,testexecution,create_time,rw_method,queue_depth,io_size):
    print '************get_Project:**************************'
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    i=0;
    while i < 6:
        new_spdk_trend_result('',float(depth_iops_list[i]),float(depth_lat_list[i]),1,create_time,5,1,1)
        #print depth_iops_list,depth_lat_list   
#####################################################

def Draw_Vhost_Scsi_QueueDepth_Detail_Chart(rw_iops,rw_lat):
    #print "randrw",randrw_iops
    os_id=0
    while os_id<1:
        draw_vhost_scsi_randrw_chart(rw_iops,rw_lat)
        draw_vhost_scsi_randwrite_chart(randwrite_iops,randwrite_lat)
        draw_vhost_scsi_randread_chart(randread_iops,randread_lat)
        draw_vhost_scsi_read_chart(read_iops,read_lat)
        draw_vhost_scsi_write_chart(write_iops,write_lat)
        draw_vhost_scsi_rw_chart(rw_iops,rw_lat)
        os_id +=1 
    return 0

def main():
    #print "$$$$$$$$",rw_iops,rw_lat
    #create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    Draw_QueueDepth_Detail_Chart(rw_iops,rw_lat)
    #Draw_Vhost_Scsi_QueueDepth_Detail_Chart(rw_iops,rw_lat)
    #get_testexecution_list()
#if '__main__' == __name__:
#    main()

