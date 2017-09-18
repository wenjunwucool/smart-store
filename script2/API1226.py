# -*- coding: utf-8 -*- 
from API1226 import *
from upload_rw_method import *

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
def Draw_Spdk_QueueDepth_Detail_Chart():
    get_result_from_fio_log()
    read_iops=Total_iops_list[0:8]
    write_iops=Total_iops_list[8:16]
    rw_iops=Total_iops_list[32:40]
    randread_iops=Total_iops_list[16:24]
    randwrite_iops=Total_iops_list[24:32]
    randrw_iops=Total_iops_list[40:48]

    read_lat=Total_lat_list[0:8]
    write_lat=Total_lat_list[8:16]
    rw_lat=Total_lat_list[32:40]
    randread_lat=Total_lat_list[16:24]
    randwrite_lat=Total_lat_list[24:32]
    randrw_lat=Total_lat_list[40:48]
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

def Draw_Vhost_Scsi_QueueDepth_Detail_Chart():
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

'''def Draw_Spdk_QueueDepth_Detail_Chart():
    Draw_QueueDepth_Detail_Chart()
'''
#if '__main__' == __name__:
#    main()

