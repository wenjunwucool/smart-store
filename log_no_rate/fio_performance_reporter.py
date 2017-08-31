#!/bin/python

import re
import os
import sys
from functools import wraps

aggrb = ' '
iops_set = {}
lat_set = {}
cpu_usage_set = {}
Total_iops=0
def get_regx_str(regx, string):
    pattern = re.compile(regx)
    result = pattern.search(string)
    if result is None:
        return False
    if len(result.groups()) == 1: 
        return result.groups()[0]
    else:
        return result.groups()

def open_file(f): 
    @wraps(f)
    def process(file_path):
        with open(file_path, 'r') as fh:
            f(fh)
    return process

@open_file
def get_aggrb(file_handle):
    global aggrb
    regx = r"(?<=aggrb=)([0-9]+\.?[0-9]*[K|M|G]B\/s)"
    for line in file_handle:
        aggrb = get_regx_str(regx, line)
        if aggrb:
            if 'KB' in aggrb:
                aggrb = float(aggrb.strip("KB/s"))
            elif 'MB' in aggrb:
                aggrb = float(aggrb.strip("MB/s")) * 1024
            elif 'GB' in aggrb:
                aggrb = float(aggrb.strip("GB/s")) * 1024 * 1024
            break

@open_file
def get_iops(file_handle):
    global iops_set
    regx = r"(?<=IOPS=)([0-9]+\.?[0-9])"        
    job_num = 0
    for line in file_handle:
        iops = 0
        iops = get_regx_str(regx, line)
        if iops:
            iops_set[job_num] = iops
            job_num += 1

@open_file
def get_latency(file_handle):
    global lat_set

    regx_u = r"[^sc]lat \(usec\): min=[ ]*\d+\.?\d*, max=[ ]*\d+\.?\d*[K]?, avg=[ ]*(\d+\.?\d*), stdev=[ ]*\d+\.?\d*"
    regx_m = r"[^sc]lat \(msec\): min=[ ]*\d+\.?\d*, max=[ ]*\d+\.?\d*[K]?, avg=[ ]*(\d+\.?\d*), stdev=[ ]*\d+\.?\d*"
    job_num = 0
    for line in file_handle:
        latency_u = 0
        latency_m = 0
        latency_u = get_regx_str(regx_u, line)
        latency_m = get_regx_str(regx_m, line)
        if latency_u or latency_m:
            if latency_u:
                lat_set[job_num] = latency_u
            else:
                lat_set[job_num] = float(latency_m) * 1000
            job_num += 1

@open_file
def get_cpu_usage(file_handle):
    global cpu_usage_set

    regx = r"  cpu *: usr=(\d+\.?\d*)%, sys=(\d+\.?\d*)%, ctx=\d+, majf=\d+, minf=\d+"
    job_num = 0
    for line in file_handle:
        cpu_usage = ()

        cpu_usage = get_regx_str(regx, line)        
        if cpu_usage:
            if len(cpu_usage) == 2:
                usage_temp = {}
                usage_temp['usr'] = float(cpu_usage[0])
                usage_temp['sys'] = float(cpu_usage[1])
                cpu_usage_set[job_num] = usage_temp
                job_num += 1
            else:
                print "Not got usr or sys usage, please check!!!"
                sys.exit()
        
def compute_iops():
    global iops_set
    total_iops = 0

    for iops in iops_set.values():
        total_iops += float(iops)

    return total_iops

def compute_latency():
    global iops_set
    global lat_set
    total_iops = 0
    total_latency = 0
    
    for key in iops_set.keys():
        if key not in lat_set.keys():
            print "iops and latency not match!!!"
            sys.exit()
        total_iops += float(iops_set[key])
        total_latency += float(iops_set[key]) * float(lat_set[key])       

    average_latency = total_latency / total_iops

    return average_latency

def compute_cpu_usage():
    global cpu_usage_set
    total_cpu_usr_usage = 0
    total_cpu_sys_usage = 0

    for value in cpu_usage_set.values():
        total_cpu_usr_usage += value['usr']
        total_cpu_sys_usage += value['sys']

    return (total_cpu_usr_usage, total_cpu_sys_usage)

#if __name__ == "__main__":
def main():
    if len(sys.argv) < 1:
        print "You must imput a file path"
        sys.exit()
    if not os.path.isfile(sys.argv[1]):
        print "The file does not exist!!!"
        sys.exit()

    iops = 0
    latency = 0

    file_path = sys.argv[1] 
    get_aggrb(file_path) 
    get_iops(file_path)
    get_latency(file_path)
    get_cpu_usage(file_path)
    print "iops_set:      ", iops_set
    print "latency_set:   ", lat_set
    #print "cpu_usage_set: ", cpu_usage_set
    iops = compute_iops()
    Total_iops=iops
    latency = compute_latency()
    cpu_usage = compute_cpu_usage()

    print "Average rw_speed: ", aggrb
    print "Total_iops:       ",iops
    print "Average_latency:  ", latency
    print "cpu usr usage:     %.2f%%" % cpu_usage[0]
    print "cpu sys usage:     %.2f%%" % cpu_usage[1]
main()
