# -*- coding: utf-8 -*- 
import requests
import json
from requests.auth import HTTPBasicAuth
from fio_performance_reporter import *
import time
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
    url = '{server_add}/api/dpdk/myresult/1/'.format(server_add=SERVER,project='dpdk') 
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

def get_testrecord_list():
    url ='{server_add}/api/{project}/testrecord/1/'.format(server_add=SERVER,project='dpdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()

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

####################### spdk testrecord ##############################
def get_spdk_perf_result_list():
    url='{server_add}/api/{project}/spdk_perf_result/1/'.format(server_add=SERVER,project='spdk') 
    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    #r = requests.get(url)
    print r.url
    print r.status_code
    print type(r.json()), r.json()

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


