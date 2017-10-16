#!/usr/bin/env python
# BSD LICENSE
#
# Copyright(c) 2010-2014 Intel Corporation. All rights reserved.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of Intel Corporation nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import time
import os
import sys
import pdb
import re
from test_case import TestCase
from exception import VerifyFailure
from Test_base_utils import write_fio_config, generate_nvmf_tgt_file
from Nvmf_perf_host import generate_conf, run_all_testcase

nvmfbackend = ["nvme_virtual",]


class TestPerf(object):

    def set_up_all(self, test_case_obj, backendname):
        """
        Run at the start of each test suite.
        fio Prerequisites
        """
        if self.nic == "ConnectX4":
            self.tester.send_expect("modprobe mlx5_core", "#", 5)
            self.tester.send_expect("modprobe mlx5_ib", "#", 5)
        if self.nic == "ConnectX3":
            self.tester.send_expect("modprobe mlx4_en", "#", 5)
            self.tester.send_expect("modprobe mlx4_core", "#", 5)
            self.tester.send_expect("modprobe mlx4_ib", "#", 5)
        if self.nic == "chelsio_40gb":
            self.tester.send_expect("modprobe cxgb4", "#", 5)
            self.tester.send_expect("modprobe iw_cxgb4", "#", 5)
        self.backend = backendname
        self.tester_ports = []
        self.dut_ports = []
        self.dut_ports_all = self.dut.get_ports()
        self.tester_ports_all = self.tester.get_ports()
        self.is_port = self._get_nic_driver(self.nic)
        for i, self.dut_port in enumerate(self.dut_ports_all[1]):
            if self.dut_port == self.is_port + '\r':
                self.dut_port_nic = self.dut_ports_all[0][i]
                self.dut_ports.append(self.dut_port_nic)
        for j, self.tester_port in enumerate(self.tester_ports_all[1]):
            if self.tester_port == self.is_port + '\r':
                self.tester_port_nic = self.tester_ports_all[0][j]
                self.tester_ports.append(self.tester_port_nic)
        self.verify(len(self.dut_ports) >= 1, "Insufficient ports")
        self.dut_port_0_inf = self.dut_ports[1]
        self.tester_port_0_inf = self.tester_ports[0]
        self.dut_ips = {'net_seg_3': "192.168.3.11"}
        self.tester_ips = {'net_seg_3': "192.168.3.2"}
        self.dut.send_expect("cd %s " % self.dut.base_dir, "# ", 5)
        self.initial_real_path = self.dut.base_dir
        self.dut_utils_path = self.initial_real_path + "/etc/spdk"
        self.dut_iscsi_config_path = self.initial_real_path + "/etc/spdk/iscsi.conf.in"
        self.dut_nvmf_config_path = self.initial_real_path + "/etc/spdk/nvmf.conf.in"
        self.dut_fiotest_path = self.dut_utils_path
        test_suite_path = os.getcwd() + "/../tests"
        self.tester_utils_path = "%s/lib/" % test_suite_path
        self.tester_utils_file = self.tester_utils_path + "Test_base_utils.py"
        self.copy_file_to_dut(self.tester_utils_file, self.dut_utils_path)
        if self.backend != "nvmf_aiobackend":
            self.dut.send_expect(
                'sed -i "s/  AIO/#  AIO/" %s' %
                self.dut_nvmf_config_path, "# ", 10)
            self.dut.send_expect(
                'sed -i "s#/dev/sdb#/dev/device1#" %s' %
                self.dut_nvmf_config_path, "# ", 10)
            self.dut.send_expect(
                'sed -i "s#/dev/sdc#/dev/device2#" %s' %
                self.dut_nvmf_config_path, "# ", 10)
        self.dut.send_expect(
            'sed -i "s/#MaxQueueDepth 128/MaxQueueDepth 1024/" %s' %
            self.dut_nvmf_config_path, "# ", 10)
        self.dut.send_expect(
            'sed -i "s/#MaxIOSize 131072/MaxIOSize 131072/" %s' %
            self.dut_nvmf_config_path, "# ", 10)
        self.dut.send_expect(
            'sed -i "s/TransportId/#TransportId/" %s' %
            self.dut_nvmf_config_path, "# ", 10)
        self.dut.send_expect(
            'sed -i "s/RetryCount 4/#RetryCount 4/" %s' %
            self.dut_nvmf_config_path, "# ", 10)
        self.dut.send_expect(
            "sed -i 's/192.168.2.21/192.168.1.11/' %s" %
            self.dut_iscsi_config_path, "# ", 10)
        self.dut.send_expect(
            "sed -i 's/192.168.2.0/192.168.1.0/' %s" %
            self.dut_iscsi_config_path, "# ", 10)

    def set_up(self):
        if self.backend in nvmfbackend:
            self.tester.send_expect(
                "ifconfig %s %s" %
                (self.tester_port_0_inf, self.tester_ips['net_seg_3']), "# ", 5)
            self.dut.send_expect(
                "ifconfig %s %s" %
                (self.dut_port_0_inf, self.dut_ips['net_seg_3']), "# ", 5)
            self.create_nvmf_tgt_config()
            #self.dut.send_expect(
            #    "ps -ef|grep nvmf_tgt|grep -v grep|awk '{print $2}'|xargs kill -15 & ",
            #    "# ",
            #    200)
            time.sleep(10)
            self.dut.send_expect("NRHUGE=6144 ./scripts/setup.sh", "#", 200)
            self.dut.send_expect(
                "./app/nvmf_tgt/nvmf_tgt -c nvmf.conf >>/root/spdk/TestSPDK.log 2>&1 &", "# ", 200)
            time.sleep(60)
            print "Waiting for connecting nvmf target..."
            self.dut.send_expect("modprobe nvme-rdma", "# ", 5)
            self.dut.send_expect("modprobe nvme-fabrics", "# ", 5)
            #self.dut.send_expect(
            #    "nvme discover -t rdma -a 192.168.3.11 -s 4420", "# ", 5)

    def create_nvmf_tgt_config(self):
        self.dut.send_expect(
            "rm -rf nvmf.conf && cp etc/spdk/nvmf.conf.in nvmf.conf ", "# ", 200)
        self.dut.send_expect(
            "python etc/spdk/Test_base_utils.py generate_nvmf_tgt_file %s nvmf.conf " %
            self.backend, "# ", 200)

    def copy_file_to_dut(self, file_in_tester, dut_file_path):
        self.dut.session.copy_file_to(file_in_tester)
        file_name = file_in_tester.split('/')[-1]
        self.dut.send_expect("mv -f /root/%s %s" %
                             (file_name, dut_file_path), "# ", 5)

    def kill_dut_process(self, process):
        command = "ps aux | grep {0} | grep -v grep | awk '{{print $2}}'".format(
            process)
        out = self.dut.alt_session.send_expect(command, "# ", 10)
        if not out:
            print "There is no process [ {0} ] in dut!!!".format(process)
        else:
            self.dut.alt_session.send_expect(
                "kill -15 %s" % out.splitlines()[0], "# ", 10)
            time.sleep(60)
            out = self.dut.alt_session.send_expect(command, "# ", 10)
            if out:
                print "kill dut process [ {0} ] failed!!!".format(process)

    def kill_target(self):
        """
        Kill nvmf target when finish one test case
        """
        if self.backend in nvmfbackend:
            self.tester.send_expect(
                'nvme disconnect -n "nqn.2016-06.io.spdk:cnode1"', "# ")
            self.tester.send_expect(
                'nvme disconnect -n "nqn.2016-06.io.spdk:cnode2"', "# ")
            self.kill_dut_process("nvmf_tgt")

    def test_nvmf_perf_host1(self):
       	generate_conf()
       	time.sleep(15)
       	run_all_testcase(1)


    def tear_down(self):
        """
        Run after each test case.
        """
        self.kill_target()
