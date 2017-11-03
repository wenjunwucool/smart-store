import re
import sys
from subprocess import check_call,check_output
		
def generate_iscsi_file(backend, filename):
    if backend == "iscsi_nvme" or backend == "iscsi_rxtxqueue":
        output = check_output("lspci -nnn", shell=True)
        bus_numbers = re.findall("([0-9][0-9]:[0-9][0-9].[0-9]) Non-Volatile memory controller", output)
        nvme_ctrl_num = len(bus_numbers)
        all_luns = int(nvme_ctrl_num)
        filedesc = open(filename, 'w+')
        filedesc.write("\n[Nvme] \n")
        for i, value in enumerate(bus_numbers):
            filedesc.write('\n  TransportId "trtype:PCIe traddr:0000:{}" Nvme{} \n'.format(value, i))
        filedesc.write("  RetryCount {} \n".format(nvme_ctrl_num))
        filedesc.write("  Timeout 0 \n")
        filedesc.write("  ActionOnTimeout None \n")
        filedesc.write("  AdminPollRate 100000 \n")
        filedesc.write("  HotplugEnable Yes \n")
        idx = 0
        for i in range(all_luns):
            target_id = idx + 1
            filedesc.write("\n[TargetNode" + str(target_id) + "]\n")
            filedesc.write("  TargetName disk" + str(target_id) + "\n")
            filedesc.write("  Mapping PortalGroup1 InitiatorGroup1\n")
            filedesc.write("  AuthMethod Auto\n")
            filedesc.write("  AuthGroup  AuthGroup1\n")
            filedesc.write("  UseDigest Auto\n")
            filedesc.write("  QueueDepth 128\n")
            filedesc.write("  LUN0 Nvme" + str(idx) + "n1" + "\n")
            idx = idx + 1
        filedesc.close()

    if backend == "iscsi_aiobackend":
        filedesc = open(filename, 'w+')
        filedesc.write("\n[AIO] \n")
        filedesc.write("  AIO /dev/sdf AIO0\n")
        filedesc.write("  AIO /dev/sde AIO1\n")
        #default configure aio mode with 2 luns
        all_luns = 2
        idx = 0
        for i in range(all_luns):
            target_id = idx + 1
            filedesc.write("\n[TargetNode" + str(target_id) + "]\n")
            filedesc.write("  TargetName disk" + str(target_id) + "\n")
            filedesc.write("  Mapping PortalGroup1 InitiatorGroup1\n")
            filedesc.write("  AuthMethod Auto\n")
            filedesc.write("  AuthGroup  AuthGroup1\n")
            filedesc.write("  UseDigest Auto\n")
            filedesc.write("  QueueDepth 128\n")
            filedesc.write("  LUN0 AIO" + str(idx) + "\n")
            idx = idx + 1
        filedesc.close()

    if backend == "iscsi_malloc":
        all_luns = 2
        idx = 0
        filedesc = open(filename, 'w+')
        filedesc.write("\n[Malloc] \n")
        filedesc.write("  NumberOfLuns 2\n")
        filedesc.write("  LunSizeInMB 128\n")
        filedesc.write("  BlockSize 512\n")
        for i in range(all_luns):
            target_id = idx + 1
            filedesc.write("\n[TargetNode" + str(target_id) + "]\n")
            filedesc.write("  TargetName disk" + str(target_id) + "\n")
            filedesc.write("  Mapping PortalGroup1 InitiatorGroup1\n")
            filedesc.write("  AuthMethod Auto\n")
            filedesc.write("  AuthGroup  AuthGroup1\n")
            filedesc.write("  UseDigest Auto\n")
            filedesc.write("  QueueDepth 128\n")
            filedesc.write("  LUN0 Malloc" + str(idx) + "\n")
            idx = idx + 1
        filedesc.close()

    if backend == "iscsi_multiconnection":
        output = check_output("lspci -nnn", shell=True)
        bus_numbers = re.findall("([0-9][0-9]:[0-9][0-9].[0-9]) Non-Volatile memory controller", output)
        nvme_ctrl_num = len(bus_numbers)
        all_luns = int(nvme_ctrl_num)
        filedesc = open(filename, 'w+')
        filedesc.write("\n[Nvme] \n")
        for i, value in enumerate(bus_numbers):
            filedesc.write('TransportID "trtype:PCIe traddr:0000:{}" Nvme{}\n'.format(value, i))
        filedesc.write("  RetryCount 128 \n")
        filedesc.write("  Timeout 0 \n")
        filedesc.write("  ActionOnTimeout None \n")
        filedesc.write("  AdminPollRate 100000 \n")
        filedesc.write("  HotplugEnable Yes \n")
        filedesc.write("\n[Split] \n")
        filedesc.write("  Split Nvme0n1 22 1 \n")
        filedesc.write("  Split Nvme1n1 22 1 \n")
        filedesc.write("  Split Nvme2n1 22 1 \n")
        filedesc.write("  Split Nvme3n1 22 1 \n")
        filedesc.write("  Split Nvme4n1 22 1 \n")
        filedesc.write("  Split Nvme5n1 18 1 \n")
        idx = 0
        target_id = 1
        all_nodes = 22
        for i in range(all_luns):
            node = 0
            for i in range(all_nodes):
                filedesc.write("\n[TargetNode" + str(target_id) + "]\n")
                filedesc.write("  TargetName disk" + str(target_id) + "\n")
                filedesc.write("  Mapping PortalGroup1 InitiatorGroup1\n")
                filedesc.write("  AuthMethod Auto\n")
                filedesc.write("  AuthGroup  AuthGroup1\n")
                filedesc.write("  UseDigest Auto\n")
                filedesc.write("  QueueDepth 32\n")
                filedesc.write("  LUN0 Nvme" + str(idx) + "n1p" + str(node) + "\n")
                node = node + 1
                target_id = target_id + 1
            idx = idx + 1
        filedesc.close()
        check_call("sed -i '/\[TargetNode129/,$d' " + filename, shell=True)

def generate_nvmf_tgt_file(backend, filename):
    if backend == "nvmf_nvme":
        output = check_output("lspci -nnn", shell=True)
        bus_numbers = re.findall(
            "([0-9][0-9]:[0-9][0-9].[0-9]) Non-Volatile memory controller", output)
        nvme_ctrl_num = len(bus_numbers)
        all_luns = int(nvme_ctrl_num)
        idx = 0
        filedesc = open(filename, 'w+')
	filedesc.write("\n[Global] \n")
	filedesc.write("\n[Rpc] \n")
	filedesc.write(" Enable No \n 127.0.0.1 \n ")
	filedesc.write(" \n[Nvmf] \n")
	filedesc.write(" MaxQueuesPerSession 4\n MaxQueueDepth 1024\n MaxIOSize 131072\n AcceptorPollRate 10000\n")
        filedesc.write("\n[Nvme] \n")
        for i, value in enumerate(bus_numbers):
            filedesc.write('TransportId "trtype:PCIe traddr:0000:{}" Nvme{} \n'.format(value, i))
        filedesc.write("NvmeRetryCount 6 \n")
        filedesc.write("Timeout 0 \n")
        filedesc.write("ActionOnTimeout None \n")
        filedesc.write("AdminPollRate 100000 \n")
        filedesc.write("HotplugEnable Yes \n")
        for i in range(all_luns):
            target_id = idx + 1
            filedesc.write("\n[Subsystem" + str(target_id) + "]\n")
            filedesc.write("  NQN nqn.2016-06.io.spdk:cnode" + str(target_id) + "\n")
            filedesc.write("  Core 0\n")
            filedesc.write("  AllowAnyHost Yes\n")
            filedesc.write("  Listen RDMA 192.168.3.11:4420\n")
            filedesc.write("  SN SPDK" + str(target_id) + "\n")
            filedesc.write("  Namespace Nvme" + str(idx) + "n1" + "\n")
            idx = idx + 1
        filedesc.close()

    if backend == "nvmf_malloc":
        #default configure malloc with 2 luns
        all_luns = 2
        idx = 0
        filedesc = open(filename, 'w+')
	filedesc.write("\n[Global] \n")
	filedesc.write("\n[Rpc] \n")
	filedesc.write(" Enable No \n 127.0.0.1 \n ")
	filedesc.write("\n[Malloc]")
	filedesc.write("\nNumberOfLuns 2 ")
	filedesc.write("\nLunSizeInMB 64 \n ")
	filedesc.write("\n[Nvmf] \n MaxQueuesPerSession 4\n MaxQueueDepth 1024\n MaxIOSize 131072\n AcceptorPollRate 10000\n")
	filedesc.write("\n[Nvme] \n Timeout 0 \n ActionOnTimeout None\n AdminPollRate 100000\n HotplugEnable No\n")
        for i in range(all_luns):
            target_id = idx + 1
            filedesc.write("\n[Subsystem" + str(target_id) + "]\n")
            filedesc.write("  NQN nqn.2016-06.io.spdk:cnode" + str(target_id) +"\n")
            filedesc.write("  Core 0\n")
            filedesc.write("  AllowAnyHost Yes\n")
            filedesc.write("  Mode Virtual\n")
            filedesc.write("  Listen RDMA 192.168.3.11:4420\n")
            filedesc.write("  SN SPDK" + str(target_id) + "\n")
            filedesc.write("  Namespace Malloc" + str(idx) + "\n")
            idx = idx + 1
        filedesc.close()

    if backend == "nvmf_nvme_multiconnection":
        #default configure multiconnection with 128 luns	
        all_luns = 128
        idx = 0
        filedesc = open(filename, 'w+')
	filedesc.write("\n[Global] \n")
	filedesc.write("\n[Rpc] \n")
	filedesc.write(" Enable No \n 127.0.0.1 \n ")
	filedesc.write("\n[Nvmf] \n MaxQueuesPerSession 4\n MaxQueueDepth 1024\n MaxIOSize 131072\n AcceptorPollRate 10000\n")
	filedesc.write("\n[Nvme] \n Timeout 0 \n ActionOnTimeout None\n AdminPollRate 100000\n HotplugEnable No\n")
        for i in range(all_luns):
            target_id = idx + 1
            filedesc.write("\n[Subsystem" + str(target_id) + "]\n")
            filedesc.write("  NQN nqn.2016-06.io.spdk:cnode" + str(target_id) + "\n")
            filedesc.write("  Core 0\n")
            filedesc.write("  AllowAnyHost Yes\n")
            filedesc.write("  Listen RDMA 192.168.3.11:4420\n")
            filedesc.write("  SN SPDK" + str(target_id) + "\n")
            filedesc.write("  Namespace Malloc" + str(idx) + "\n")
            idx = idx + 1
        filedesc.close()

    if backend == "nvmf_aiobackend":
	
        filedesc = open(filename, 'w+')
	filedesc.write("\n[Global] \n")
	filedesc.write("\n[Rpc] \n")
	filedesc.write(" Enable No \n 127.0.0.1 \n ")
	filedesc.write("\n[AIO] \n")
        all_luns = 2
        idx = 0
        for i in range(all_luns):
            target_id = idx + 1
            filedesc.write("\n[Subsystem" + str(target_id) + "]\n")
            filedesc.write("  NQN nqn.2016-06.io.spdk:cnode" + str(target_id) + "\n")
	    filedesc.write("  Core 0\n")	
            filedesc.write("  AllowAnyHost Yes\n")
            filedesc.write("  Listen RDMA 192.168.3.11:4420\n")
            filedesc.write("  SN SPDK" + str(target_id) + "\n")
            filedesc.write("  Namespace AIO" + str(idx) + "\n")
            idx = idx + 1
        filedesc.close()
print """Error application Type:\n Choose application:\n nvmf_nvme \n nvmf_malloc \n nvmf_aiobackend \n nvmf_mult  iconnection\n iscsi_nvme\n iscsi_malloc\n iscsi_aiobacken\n iscsi_multiconnection \n"""

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print "usage:"
        print "  " + sys.argv[0] + " <application name> <configure file name> "
        sys.exit(1)
    backend_name = sys.argv[1]

    if str(backend_name.split('_')[0]) == "iscsi":
        iscsi_file = sys.argv[2]
        generate_iscsi_file(backend_name, iscsi_file)

    if str(backend_name.split('_')[0]) == "nvmf":
        nvmf_file = sys.argv[2]
        generate_nvmf_tgt_file(backend_name, backend_name + ".conf")
		
    else:
        print "usage:"
        print "  " + sys.argv[0] + " <application name> <configure file name> "
        print "Examples:"
        print " generate nvmf_nvme configure file:'python Test_base_utils.py nvmf_nvme nvmf_nvme.conf'"
        print " python Test_base_utils.py nvmf_malloc nvmf_malloc.conf "
        print " python Test_base_utils.py nvmf_nvme_multiconnection nvmf_multiconnection.conf "
        print " python Test_base_utils.py nvmf_aiobackend nvmf_aiobackend.conf "
        print " python Test_base_utils.py iscsi_nvme iscsi_nvme.conf "
        print " python Test_base_utils.py iscsi_aiobackend iscsi_aiobackend.conf "
        print " python Test_base_utils.py iscsi_malloc iscsi_malloc.conf "
        print " python Test_base_utils.py iscsi_multiconnection iscsi_multiconnection.conf "

