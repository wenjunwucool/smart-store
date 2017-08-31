from pexpect import pxssh
import getpass
import ConfigParser
from subprocess import call , check_call
import time

def login_target():
    try:
        s = pxssh.pxssh()
        hostname = target_ip
        #hostname = target_ip
        username = 'root'
        passwd = 'tester'
        s.login(hostname,username,passwd)
    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)

def kill_nvmf_target():
    try:
        s = pxssh.pxssh()
        hostname = target_ip
        username = 'root'
        passwd = 'tester'
        s.login(hostname,username,passwd)
        s.sendline("ps -aux|grep -v grep|grep nvmf_tgt|awk '{print $2}'|xargs kill -9 ")
        s.prompt()
        print s.before
        s.logout()
    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)
  
def generate_conf():
    global target_ip,rw_type ,io_size , runtime ,rw_method,queue_depth
    conf=ConfigParser.ConfigParser()
    conf.read("nvmf-host.conf")
    sections = conf.sections()
    queue_depth = conf.get("test","queue_depth")
    target_ip = conf.get("Server_IP","target_ip")
    rw_method = conf.get("test","rw_method")
    io_size = conf.get("test","io_size")
    runtime = conf.get("test","runtime")
    print rw_method.split(',')
    print target_ip
    print queue_depth
    print io_size
    print runtime
 
def run_perf():
    generate_conf()
    check_call("run_perf",shell=True)
 
def run_nvmf_target():
    try:
        s = pxssh.pxssh()
        hostname = target_ip
        username = 'root'
        password = 'tester'
        s.login (hostname, username, password)
        s.sendline ('/root/waikiki/spdk/app/nvmf_tgt/nvmf_tgt -c /root/waikiki/spdk/nvmf.conf &')
        s.logout()
        print "logout"
    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)

def run_all_testcast():
    for rw_type in rw_method.split(','):
        for io_size1 in io_size.split(','):
            for queue_depth1 in queue_depth.split(','):
                try:
                    if (rw_type == rw | rw_type = randrw):
                        print "/root/spdk-17.07/examples/nvme/perf/perf -q %s -w %s -s  %s -t %s -M 50 -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(queue_depth1,rw_type,io_size1,runtime)
                        call("/root/spdk-17.07/examples/nvme/perf/perf -q %s -w %s -s %s -t %s -M 50 -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(queue_depth1,rw_type,io_size1,runtime),shell=True)
                    else:
                        print "/root/spdk-17.07/examples/nvme/perf/perf -q %s -w %s -s  %s -t %s -M 50 -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(queue_depth1,rw_type,io_size1,runtime)
                        call("/root/spdk-17.07/examples/nvme/perf/perf -q %s -w %s -s %s -t %s -M 50 -r 'trtype:RDMA adrfam:IPv4 traddr:192.168.3.11 trsvcid:4420'"%(queue_depth1,rw_type,io_size1,runtime),shell=True)

                except:
                    print "examples/nvme/perf Test Case %s %s %s Failed"%(queue_depth1,rw_type,io_size1)
                else:
                    print "All test case Passed"
generate_conf()
kill_nvmf_target()
run_nvmf_target()
time.sleep(10)
run_all_testcast()
kill_nvmf_target()
