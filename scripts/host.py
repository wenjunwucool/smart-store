#!/usr/bin/env python

from subprocess import check_call, call, check_output, Popen, PIPE
import time
import os
import sys
import re
from nvmf_fio import fio_test

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

def set_up():
    ethname = []
    drivername = []
    get_ports(ethname, drivername)
    port = ethname[0].split('\n')
    driver = "mlx4_en"
    if driver in drivername:
        check_call("ifconfig %s192.168.3.2" % port[0],shell=True)
        check_call("modprobe mlx4_ib", shell=True)
    else:
        driver = "mlx5_core"
        if driver in drivername:
            check_call("ifconfig %s 192.168.3.2" % port[0],shell=True)
            check_call("modprobe mlx5_ib", shell=True)
        else:
            print "Cannot find mellanox nic"
    check_call("modprobe nvme-rdma", shell=True)
    check_call("modprobe nvme-fabrics", shell=True)
    number = 128
    for i in range(number):
        idx = i + 1
        call('nvme connect -t rdma -n "nqn.2016-06.io.spdk:cnode%s" -a 192.168.3.11 -s 4420' % idx, shell=True)

if __name__ == "__main__":
    set_up()
    fio_test('512 - 256k', '16 - 128', 'randrw', 60, 50)
