#!/usr/bin/env python

from subprocess import check_call, call, check_output, Popen, PIPE
import re
import sys
import signal
import time
import datetime
import threading

fio_template = """
[global]
thread=1
invalidate=1
rw=%(testtype)s
time_based=1
runtime=%(runtime)s
rwmixread=%(rw_mixread)d
ioengine=libaio
direct=1
bs=%(blocksize)d
iodepth=%(iodepth)d
%(verify)s
verify_dump=1

"""

verify_template = """
do_verify=1
verify=meta
verify_pattern="meta"
"""

fio_job_template = """
[job%(jobnumber)d]
filename=%(device)s

"""

def interrupt_handler(signum, frame):
    fio.terminate()
    print "FIO terminated"
    sys.exit(0)

def fio_test(io_range, queue_range, test_type, run_time, rwmixread):
    global fio
    io_range = get_range(io_range)
    queue_range = get_range(queue_range)
    io_sizes = list(power_of_2_range(io_range[0], io_range[1]))
    queue_depths = list(power_of_2_range(queue_range[0], queue_range[1]))
    test_type = str(test_type)
    run_time = int(run_time)
    rwmixread = int(rwmixread)
    verify = False
    devices = get_target_devices()
    print "Found devices: ", devices
    check_fio()
    fio_executable = '/usr/bin/fio'
    device_paths = ['/dev/' + dev for dev in devices]
    log = ""
    for size in io_sizes:
        for q_depth in queue_depths:
            sys.stdout.flush()
            signal.signal(signal.SIGTERM, interrupt_handler)
            signal.signal(signal.SIGINT, interrupt_handler)
            start_time = datetime.datetime.now()
            fio = Popen([fio_executable, '-'], stdin=PIPE)
            fio.communicate(create_fio_config(size, q_depth, device_paths, test_type, run_time, rwmixread, verify))
            fio.stdin.close()
            rc = fio.wait()
            print "FIO completed with code %d\n" % rc
            sys.stdout.flush()
            time.sleep(1)
            if rc != 0:
                log += "Failed %s at Size %d, queue depth %d\n" % (test_type, size, q_depth)
            else:
                end_time = datetime.datetime.now()
                duration = end_time - start_time
                print "duration is {0}".format(duration)

def check_fio():
    output = check_output('fio --version', shell=True)
    version = re.findall("fio-(.*)", output)
    print "fio version is", version

def get_target_devices():
    output = check_output('lsblk -l -o NAME', shell=True)
    return re.findall("(nvme[0-9]+n[0-9]+)\n", output)

def create_fio_config(size, q_depth, devices, test_type, run_time, rwmixread, verify):
    verifyfio = ""
    fiofile = fio_template % {"blocksize": size, "iodepth": q_depth, "testtype": test_type, "runtime": run_time, "rw_mixread": rwmixread, "verify": verifyfio}
    for (i, dev) in enumerate(devices):
        fiofile += fio_job_template % {"jobnumber": i, "device": dev}
    return fiofile

def set_device_parameter(devices, filename_template, value):
    for dev in devices:
        filename = filename_template % dev
        f = open(filename, 'r+b')
        f.write(value)
        f.close()

def configure_devices(devices):
    set_device_parameter(devices, "/sys/block/%s/queue/nomerges", "2")
    set_device_parameter(devices, "/sys/block/%s/queue/nr_requests", "128")
    requested_qd = 128
    qd = requested_qd
    while qd > 0:
        try:
            set_device_parameter(devices, "/sys/block/%s/device/queue_depth", str(qd))
            break
        except IOError:
            qd = qd - 1
    if qd == 0:
        print "Could not set block device queue depths."
    else:
        print "Requested queue_depth {} but only {} is supported.".format(str(requested_qd), str(qd))
    set_device_parameter(devices, "/sys/block/%s/queue/scheduler", "noop")

def power_of_2_range(start, end):
    n = convert_units(start)
    while n <= convert_units(end):
        yield n
        n = n * 2

def convert_units(num):
    if isinstance(num, type(str())):
        if not num.isdigit():
            multipliers = {'K': 1024, 'M': 1024**2, 'G': 1024**3, 'T': 1024**4}
            x = int(num[:-1])
            prefix = num[-1].upper()
            return x * multipliers[prefix]
        else:
            return int(num)
    else:
        return num

def get_range(item):
    range_string = item.split('-')
    range_list = [x.strip() for x in range_string]
    if len(range_list) == 1:
        range_list.append(range_list[0])
    return range_list
