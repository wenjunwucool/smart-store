from API1226 import *
import time 
from fio_performance_reporter import *
def draw_randwrite_chart(read_iops,read_lat):
    
    #new_dpdk_testplan(plan_id,plan_name,rw_method_id,io_size_id,queue_size_id,owner,create_time,description,del_flag):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','nvmf-target',5,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[0]),float(randwrite_lat[0]),"case_type",exe_id+1,create_time,5,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[1]),float(randwrite_lat[1]),"case_type",exe_id+2,create_time,5,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result('',float(iops_data_list[2]),float(lat_data_list[2]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(randwrite_iops[2]),float(randwrite_lat[2]),"case_type",exe_id+3,create_time,5,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[3]),float(randwrite_lat[3]),"case_type",exe_id+4,create_time,5,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[4]),float(randwrite_lat[4]),"case_type",exe_id+5,create_time,5,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[5]),float(randwrite_lat[5]),"case_type",exe_id+6,create_time,5,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[6]),float(randwrite_lat[6]),"case_type",exe_id+7,create_time,5,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[7]),float(randwrite_lat[7]),"case_type",exe_id+8,create_time,5,1,1)


########Draw randwrite Chart:###########
def draw_randread_chart(randread_iops,randread_lat):
    exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','nvmf-target',4,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(randread_iops[0]),float(randread_lat[0]),"case_type",exe_id+1,create_time,4,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[1]),float(randread_lat[1]),"case_type",exe_id+2,create_time,4,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[2]),float(randread_lat[2]),"case_type",exe_id+3,create_time,4,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[3]),float(randread_lat[3]),"case_type",exe_id+4,create_time,4,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[4]),float(randread_lat[4]),"case_type",exe_id+5,create_time,4,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[5]),float(randread_lat[5]),"case_type",exe_id+6,create_time,4,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[6]),float(randread_lat[6]),"case_type",exe_id+7,create_time,4,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[7]),float(randread_lat[7]),"case_type",exe_id+8,create_time,4,1,1)


def draw_randrw_chart(rw_iops,rw_lat):
    exe_id = get_testexecution_list()
    print "XXXXXXXXXXXXXXXXX",randrw_iops,randrw_lat
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','nvmf-target',6,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    #plan_id = 21
    #exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(randrw_iops[0]),float(randrw_lat[0]),"case_type",exe_id+1,create_time,6,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[1]),float(randrw_lat[1]),"case_type",exe_id+2,create_time,6,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[2]),float(randrw_lat[2]),"case_type",exe_id+3,create_time,6,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[3]),float(randrw_lat[3]),"case_type",exe_id+4,create_time,6,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[4]),float(randrw_lat[4]),"case_type",exe_id+5,create_time,6,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[5]),float(randrw_lat[5]),"case_type",exe_id+6,create_time,6,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[6]),float(randrw_lat[6]),"case_type",exe_id+7,create_time,6,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[7]),float(randrw_lat[7]),"case_type",exe_id+8,create_time,6,1,1)



def draw_read_chart(read_iops,read_lat):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','nvmf-target',1,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(read_iops[0]),float(read_lat[0]),"case_type",exe_id+1,create_time,1,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[1]),float(read_lat[1]),"case_type",exe_id+2,create_time,1,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[2]),float(read_lat[2]),"case_type",exe_id+3,create_time,1,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[3]),float(read_lat[3]),"case_type",exe_id+4,create_time,1,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[4]),float(read_lat[4]),"case_type",exe_id+5,create_time,1,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[5]),float(read_lat[5]),"case_type",exe_id+6,create_time,1,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[6]),float(read_lat[6]),"case_type",exe_id+7,create_time,1,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[7]),float(read_lat[7]),"case_type",exe_id+8,create_time,1,1,1)



def draw_write_chart(write_iops,write_lat):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','nvmf-target',2,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(write_iops[0]),float(write_lat[0]),"case_type",exe_id+1,create_time,2,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[1]),float(write_lat[1]),"case_type",exe_id+2,create_time,2,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[2]),float(write_lat[2]),"case_type",exe_id+3,create_time,2,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[3]),float(write_lat[3]),"case_type",exe_id+4,create_time,2,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[4]),float(write_lat[4]),"case_type",exe_id+5,create_time,2,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[5]),float(write_lat[5]),"case_type",exe_id+6,create_time,2,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[6]),float(write_lat[6]),"case_type",exe_id+7,create_time,2,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[7]),float(write_lat[7]),"case_type",exe_id+8,create_time,2,1,1)




def draw_rw_chart(rw_iops,rw_lat):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','nvmf-target',3,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[0]),float(rw_lat[0]),"case_type",exe_id+1,create_time,3,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[1]),float(rw_lat[1]),"case_type",exe_id+1,create_time,3,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[2]),float(rw_lat[2]),"case_type",exe_id+1,create_time,3,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[3]),float(rw_lat[3]),"case_type",exe_id+1,create_time,3,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[4]),float(rw_lat[4]),"case_type",exe_id+1,create_time,3,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[5]),float(rw_lat[5]),"case_type",exe_id+1,create_time,3,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[6]),float(rw_lat[6]),"case_type",exe_id+1,create_time,3,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[7]),float(rw_lat[7]),"case_type",exe_id+1,create_time,3,1,1)


    


def write_all_rw_method():
    draw_randwrite_chart()
    draw_randread_chart()
    draw_randrw_chart()
    draw_read_chart()
    draw_write_chart()
    draw_rw_chart()



#VhostScsi:

def draw_vhost_scsi_read_chart(read_iops,read_lat):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','Vhost_scsi',1,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(read_iops[0]),float(read_lat[0]),"VhostScsi",exe_id+1,create_time,1,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[1]),float(read_lat[1]),"VhostScsi",exe_id+2,create_time,1,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[2]),float(read_lat[2]),"VhostScsi",exe_id+3,create_time,1,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[3]),float(read_lat[3]),"VhostScsi",exe_id+4,create_time,1,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[4]),float(read_lat[4]),"VhostScsi",exe_id+5,create_time,1,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[5]),float(read_lat[5]),"VhostScsi",exe_id+6,create_time,1,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[6]),float(read_lat[6]),"VhostScsi",exe_id+7,create_time,1,1,1)

    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(read_iops[7]),float(read_lat[7]),"VhostScsi",exe_id+8,create_time,1,1,1)


def draw_vhost_scsi_write_chart(write_iops,write_lat):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','VhostScsi',2,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(write_iops[0]),float(write_lat[0]),"VhostScsi",exe_id+1,create_time,2,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[1]),float(write_lat[1]),"VhostScsi",exe_id+2,create_time,2,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[2]),float(write_lat[2]),"VhostScsi",exe_id+3,create_time,2,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[3]),float(write_lat[3]),"VhostScsi",exe_id+4,create_time,2,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[4]),float(write_lat[4]),"VhostScsi",exe_id+5,create_time,2,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[5]),float(write_lat[5]),"VhostScsi",exe_id+6,create_time,2,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[6]),float(write_lat[6]),"VhostScsi",exe_id+7,create_time,2,1,1)

    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(write_iops[7]),float(write_lat[7]),"VhostScsi",exe_id+8,create_time,2,1,1)


def draw_vhost_scsi_rw_chart(rw_iops,rw_lat):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','VhostScsi',3,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    exe_id = get_testexecution_list()
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[0]),float(rw_lat[0]),"VhostScsi",exe_id+1,create_time,3,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[1]),float(rw_lat[1]),"VhostScsi",exe_id+1,create_time,3,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[2]),float(rw_lat[2]),"VhostScsi",exe_id+1,create_time,3,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[3]),float(rw_lat[3]),"VhostScsi",exe_id+1,create_time,3,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[4]),float(rw_lat[4]),"VhostScsi",exe_id+1,create_time,3,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[5]),float(rw_lat[5]),"VhostScsi",exe_id+1,create_time,3,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[6]),float(rw_lat[6]),"VhostScsi",exe_id+1,create_time,3,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(rw_iops[7]),float(rw_lat[7]),"VhostScsi",exe_id+1,create_time,3,1,1)


def draw_vhost_scsi_randread_chart(randread_iops,randread_lat):
    exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','VhostScsi',4,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)

    new_spdk_perf_result('',float(randread_iops[0]),float(randread_lat[0]),"VhostScsi",exe_id+1,create_time,4,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[1]),float(randread_lat[1]),"VhostScsi",exe_id+2,create_time,4,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[2]),float(randread_lat[2]),"VhostScsi",exe_id+3,create_time,4,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[3]),float(randread_lat[3]),"VhostScsi",exe_id+4,create_time,4,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[4]),float(randread_lat[4]),"VhostScsi",exe_id+5,create_time,4,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[5]),float(randread_lat[5]),"VhostScsi",exe_id+6,create_time,4,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[6]),float(randread_lat[6]),"VhostScsi",exe_id+7,create_time,4,1,1)

    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randread_iops[7]),float(randread_lat[7]),"VhostScsi",exe_id+8,create_time,4,1,1)

    
def draw_vhost_scsi_randwrite_chart(read_iops,read_lat):
    
    #new_dpdk_testplan(plan_id,plan_name,rw_method_id,io_size_id,queue_size_id,owner,create_time,description,del_flag):
    exe_id = get_testexecution_list()
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','VhostScsi',5,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[0]),float(randwrite_lat[0]),"VhostScsi",exe_id+1,create_time,5,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[1]),float(randwrite_lat[1]),"VhostScsi",exe_id+2,create_time,5,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result('',float(iops_data_list[2]),float(lat_data_list[2]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(randwrite_iops[2]),float(randwrite_lat[2]),"VhostScsi",exe_id+3,create_time,5,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[3]),float(randwrite_lat[3]),"VhostScsi",exe_id+4,create_time,5,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[4]),float(randwrite_lat[4]),"VhostScsi",exe_id+5,create_time,5,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[5]),float(randwrite_lat[5]),"VhostScsi",exe_id+6,create_time,5,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[6]),float(randwrite_lat[6]),"VhostScsi",exe_id+7,create_time,5,1,1)

    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randwrite_iops[7]),float(randwrite_lat[7]),"VhostScsi",exe_id+8,create_time,5,1,1)


def draw_vhost_scsi_randrw_chart(rw_iops,rw_lat):
    exe_id = get_testexecution_list()
    #print "XXXXXXXXXXXXXXXXX",randrw_iops,randrw_lat
    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_dpdk_testplan('','VhostScsi',6,2,1,'wuwenzhong',create_time,"mvmf_tagret",0)
    plan_id = get_testplan_list()
    #plan_id = 21
    #exe_id = get_testexecution_list()
    #create_execution(plan_id, name, rw, io_size, queue_depth , create_time,runner,testplan, environment):
    create_execution('','1_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    #new_spdk_perf_result(result_id,iops,latency,case_type,testexecution,create_time,rw_method,queue_depth,io_size):
    #new_spdk_perf_result('',float(iops_data_list[0]),float(lat_data_list[0]),"case_type",exe_id+1,create_time,2,1,1)
    new_spdk_perf_result('',float(randrw_iops[0]),float(randrw_lat[0]),"VhostScsi",exe_id+1,create_time,6,1,1)

    create_execution('','2_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[1]),float(randrw_lat[1]),"VhostScsi",exe_id+2,create_time,6,1,1)

    create_execution('','4_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[2]),float(randrw_lat[2]),"VhostScsi",exe_id+3,create_time,6,1,1)

    create_execution('','8_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[3]),float(randrw_lat[3]),"VhostScsi",exe_id+4,create_time,6,1,1)

    create_execution('','16_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[4]),float(randrw_lat[4]),"VhostScsi",exe_id+5,create_time,6,1,1)

    create_execution('','32_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[5]),float(randrw_lat[5]),"VhostScsi",exe_id+6,create_time,6,1,1)

    create_execution('','64_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[6]),float(randrw_lat[6]),"VhostScsi",exe_id+7,create_time,6,1,1)
    create_execution('','128_Queue_depth',1,1,1,create_time,'wu',plan_id,1)
    new_spdk_perf_result('',float(randrw_iops[7]),float(randrw_lat[7]),"VhostScsi",exe_id+8,create_time,6,1,1)


def write_vhost_scsi_detail_all():
    draw_randwrite_chart()
    draw_randread_chart()
    draw_randrw_chart()
    draw_read_chart()
    draw_write_chart()
    draw_rw_chart()


def Draw_Vhost_Scsi_Trend_Chart():
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

    print 'max_read_iops',max_read_iops
    print 'max_write_iops',max_write_iops

    create_time=time.strftime('%Y-%m-%d %x',time.localtime())
    new_vhost_scsi_trend_result('',max_read_iops,max_read_lat,1,create_time,1,1,1)
    new_vhost_scsi_trend_result('',max_write_iops,max_write_lat,1,create_time,2,1,1)
    new_vhost_scsi_trend_result('',max_rw_iops,max_rw_lat,1,create_time,3,1,1)
    new_vhost_scsi_trend_result('',max_randread_iops,max_randread_lat,1,create_time,4,1,1)
    new_vhost_scsi_trend_result('',max_randwrite_iops,max_randwrite_lat,1,create_time,5,1,1)
    new_vhost_scsi_trend_result('',max_randrw_iops,max_randrw_lat,1,create_time,6,1,1)

