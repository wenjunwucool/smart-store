from pexpect import pxssh
import getpass
import ConfigParser
from subprocess import call , check_call,Popen,PIPE
import time
import os

#generate perf_host argv from nvmf-host.conf
def generate_conf():
    global rw_type, io_size, runtime, rw_method, queue_depth
    conf=ConfigParser.ConfigParser()
    pwd = os.path.dirname(__file__)
    conf_file = pwd + '/nvmf-host.conf'
    conf.read(conf_file)
    sections = conf.sections()
    spdk_path = conf.get("spdk_path","spdk_path")
    queue_depth = conf.get("test","queue_depth")
    rw_method = conf.get("test","rw_method")
    io_size = conf.get("test","io_size")
    runtime = conf.get("test","runtime")
    print rw_method.split(',')
    print queue_depth
    print io_size
    print runtime
 

def run_all_testcase():
    global case_num = 1
    for rw_type in rw_method.split(','):
        for io_size1 in io_size.split(','):
            for queue_depth1 in queue_depth.split(','):
                #try:
                if num == i:
                    if (rw_type == 'rw' or rw_type == 'randrw'):
                        print "%s/examples/nvme/perf/perf -q %s -w %s -s  %s -t %s -M 50 -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(spdk_path,queue_depth1,rw_type,io_size1,runtime)
                        out = call("%s/examples/nvme/perf/perf -q %s -w %s -s %s -t %s -M 50 -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(spdk_path,queue_depth1,rw_type,io_size1,runtime),shell=True)
                        time.sleep(1)
                    else:
                        print "%s/examples/nvme/perf/perf -q %s -w %s -s  %s -t %s  -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(spdk_path,queue_depth1,rw_type,io_size1,runtime)
                        out = call("%s/examples/nvme/perf/perf -q %s -w %s -s %s -t %s -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(spdk_path,queue_depth1,rw_type,io_size1,runtime),shell=True)
                        time.sleep(1)
                case_num = case_num + 1

