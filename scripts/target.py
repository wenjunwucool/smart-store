import time
import os
import sys
import re


class Start_target:

def get_ports(ethname,drivername):
    output = check_output("lspci -nn|grep Mellanox", shell=True)
    pci_devices_info = re.findall("([0-9][0-9]:[0-9][0-9].[0-9])", output)
    for i,value in enumerate(pci_devices_info):
        eth = check_output("ls --color=never /sys/bus/pci/devices/0000:%s/net" % value, shell=True)
        if eth != 0:
            out = check_output("ethtool -i %s" % eth, shell=True)
            status = re.findall(r"driver:\s+(.*)", out)
            if status:
                drivername.append(status[0])
                ethname.append(eth)
    return ethname, drivername

def generate_nvmf_tgt_file(filename):
    check_call("sed -i '/\[Nvme/,$d' " + filename, shell=True)
    output = check_output("lspci -nnn", shell=True)
    bus_numbers = re.findall("([0-9][0-9]:[0-9][0-9].[0-9]) Non-Volatile memory controller", output)
    nvme_ctrl_num = len(bus_numbers)
    all_luns = int(nvme_ctrl_num)
    filedesc = open(filename, 'a')
    filedesc.write("\n[Gpt]\n")
    filedesc.write("\nDisable Yes\n")
    filedesc.write("\n[Nvme] \n")
    for i, value in enumerate(bus_numbers):
        filedesc.write('\n  TransportId "trtype:PCIe traddr:0000:{}" Nvme{} \n'.format(value, i))
    filedesc.write("\n  NvmeRetryCount {} \n".format(all_luns))
    filedesc.write("\n  ResetControllerOnTimeout Yes \n")
    filedesc.write("\n  NvmeTimeoutValue 30 \n")
    filedesc.write("\n  AdminPollRate 100000 \n")
    filedesc.write("\n[Split] \n")
    filedesc.write("  Split Nvme0n1 64 1 \n")
    filedesc.write("  Split Nvme1n1 64 1 \n")
    idx = 0
    target_id = 1
    all_nodes = 64
    for i in range(all_luns):
        node = 0
        for i in range(all_nodes):
            filedesc.write("\n[Subsystem" + str(target_id) + "]\n")
            filedesc.write("  NQN nqn.2016-06.io.spdk:cnode" + str(target_id) + "\n")
            filedesc.write("  Core 0\n")
            filedesc.write("  Listen RDMA 192.168.3.11:4420\n")
            filedesc.write("  SN SPDK" + str(target_id) + "\n")
            filedesc.write("  Namespace Nvme" + str(idx) + "n1p" + str(node) + "\n")
            node = node + 1
            target_id = target_id + 1
        idx = idx + 1
    filedesc.close()

def set_up():
    ethname = []
    drivername = []
    get_ports(ethname, drivername)
    port = ethname[0].split('\n')
    driver = "mlx4_en"
    if driver in drivername:
        check_call("ifconfig %s192.168.3.11" % port[0],shell=True)
        check_call("modprobe mlx4_ib", shell=True)
    else:
        driver = "mlx5_core"
        if driver in drivername:
            check_call("ifconfig %s 192.168.3.11" % port[0],shell=True)
            check_call("modprobe mlx5_ib", shell=True)
        else:
            print "Cannot find mellanox nic"
    spdk_path = "/root/spdk"
    dpdk_path = "/root/spdk/dpdk"
    spdk_gitURL = r"https://github.com/spdk/spdk.git"
    dpdk_gitURL = r"https://github.com/spdk/dpdk.git"
    if os.path.exists("%s" % spdk_path) is True:
        ret = os.system("cd %s && git pull" % spdk_path)
    else:
        print "git clone %s" % spdk_gitURL
        ret = os.system("git clone %s" % spdk_gitURL)
        if ret is not 0:
            print "Clone spdk failed!!!"
            raise EnvironmentError
    if os.path.exists("%s" % dpdk_path) is True:
        ret = os.system("cd %s && git pull" % dpdk_path)
        if ret is not 0:
            ret = os.system("rm -rf %s" % dpdk_path)
            print "git clone %s" % dpdk_gitURL
            ret = os.system("git clone %s" % dpdk_gitURL)
            if ret is not 0:
                print "Clone dpdk failed!!!"
                raise EnvironmentError
    else:
        print "git clone %s" % dpdk_gitURL
        ret = os.system("git clone %s" % dpdk_gitURL)
        if ret is not 0:
            print "Clone dpdk failed!!!"
            raise EnvironmentError
    check_call("modprobe ib_addr", shell=True)
    check_call("modprobe ib_cm", shell=True)
    check_call("modprobe ib_core", shell=True)
    check_call("modprobe ib_mad", shell=True)
    check_call("modprobe ib_sa", shell=True)
    check_call("modprobe ib_ucm", shell=True)
    check_call("modprobe ib_umad", shell=True)
    check_call("modprobe ib_uverbs", shell=True)
    check_call("modprobe iw_cm", shell=True)
    check_call("modprobe rdma_cm", shell=True)
    check_call("modprobe rdma_ucm", shell=True)
    check_call("NRHUGE=12288 %s/scripts/setup.sh" % spdk_path, shell=True)
    check_call("make clean", shell=True)
    check_call("./configure --with-rdma", shell=True)
    check_call("make -j", shell=True)
    nvmf_config_path = %s + '/etc/spdk/nvmf.conf.in'
    nvmf_tgt_file = %s + '/nvmf.conf'
    check_call('sed -i "s/  AIO/#  AIO/" %s' % nvmf_config_path, shell=True)
    check_call('sed -i "s/#MaxQueueDepth 128/MaxQueueDepth 1024/" %s' % nvmf_config_path, shell=True)
    check_call('sed -i "s/#MaxIOSize 131072/MaxIOSize 131072/" %s' % nvmf_config_path, shell=True)
    check_call("rm -rf %s && cp %s %s " % (nvmf_tgt_file, nvmf_config_path, nvmf_tgt_file), shell=True)
    generate_nvmf_tgt_file(nvmf_tgt_file)
    cmd = "./app/nvmf_tgt/nvmf_tgt -c nvmf.conf"
    out = Popen(cmd, shell=True)
    rc = out.wait()
    if rc != 0:
        print "start to run nvmf_tgt failed"

