from subprocess import call 
from time import sleep

class Nvme_cli:
    def test_case1(self,num):
        if num == 1:
            ##Test Case 1: nvem-list command:
            call("cd /home/wenzhong/nvme-cli && ./nvme list",shell=True)
            sleep(2)
    def test_case2(self,num):
        if num == 2:
            ##Test Case 2: nvme id-ctrl command:
            call("cd /home/wenzhong/nvme-cli && ./nvme id-ctrl 0000:81:00.0",shell=True)
            sleep(2)
    def test_case3(self,num):
        if num == 3:
            ##Test Case 3: nvme id-ns command:
            call("cd /home/wenzhong/nvme-cli && ./nvme id-ns 0000:81:00.0",shell=True)
            sleep(2)
    def test_case4(self,num):
        if num == 4:
            ##Test Case 4: nvme liat-ns command:
            call("cd /home/wenzhong/nvme-cli && ./nvme list-ns 0000:81:00.0 -n 1",shell=True)
            sleep(2)
    def test_case5(self,num):
        if num == 5:
            ##Test Case 5: nvme create-ns command:
            #Note P3700 not support create-ns because it only one namespace
            #call("./nvme create-ns 0000.81:00.0 -s 0x1400000 -c 0x1400000 -f 0 -d 0 -m 0")
            sleep(2)
            pass
    def test_case6(self,num):
        if num == 6:
            ##Test Case 6:nvme delete-ns command:
            #Must create-ns frist,then can delete the namespace
            #call(./nvme delete-ns 0000:81:00.0  -n 2)
            pass
    def test_case7(self,num):
        if num == 7:
            ##Test Case 7: nvme attach-ns command: NOTICE: Must create a namespace frist 
            #call("./nvme attach-ns 0000:81:00.0 -n 1",shell=True)
            pass#sleep(2)
    def test_case8(self,num):
        if num == 8:
            ##Test Case 8: nvme detach-ns command:
            #call("./nvme detach-ns 0000:81:00.0 -n 1",shell=True)
            pass#sleep(2)
    def test_case9(self,num):
        if num == 9:
            ##Test Case 9: nvme list-ctrl command:
            call("cd /home/wenzhong/nvme-cli && ./nvme list-ctrl 0000:81:00.0",shell=True)
            sleep(2)
    def test_case10(self,num):
        if num == 10:
            ##Test Case 10: nvme get-ns-id command:
            call("cd /home/wenzhong/nvme-cli && ./nvme get-ns-id 0000:81:00.0",shell=True)
            sleep(2)
    def test_case11(self,num):
        if num == 11:
            ##Test Case 11: nvme get-log command
            call("cd /home/wenzhong/nvme-cli && ./nvme get-log 0000:81:00.0 -n 1 -i 1 -l 100",shell=True)
            sleep(2)
    def test_case12(self,num):
        if num == 12:
            ##Test Case 12: nvme fw-log command:
            call("cd /home/wenzhong/nvme-cli && ./nvme fw-log 0000:81:00.0",shell=True)
            sleep(2)
    def test_case13(self,num):
        if num == 13:
            ##Test Case 13: nvme smart-log command:
            call("cd /home/wenzhong/nvme-cli && ./nvme smart-log 0000:81:00.0",shell=True)
            sleep(2)
    def test_case14(self,num):
        if num == 14:
            ##Test Case 14: nvme error-log command
            call("cd /home/wenzhong/nvme-cli && ./nvme error-log 0000:81:00.0",shell=True)
            sleep(2)
            call("cd /home/wenzhong/nvme-cli && ./nvme error-log 0000:81:00.0 -n 1 -e 3 ",shell=True)
            sleep(2)
    def test_case15(self,num):
        if num == 15:
            ##Test Case 15: nvme get-feature command
            call("cd /home/wenzhong/nvme-cli && ./nvme get-feature 0000:81:00.0 -n 1 -f 1 -s 1 -l 100",shell=True)
            sleep(2)
    def test_case16(self,num):
        if num == 16:
            ##Test Case 16: nvme set-feature command
            #call("./nvme set-feature -n 1 -f 1 -v 1 -l 100 0000:81:00.0",shell=True)
            pass#sleep(2)
    def test_case17(self,num):
        if num == 17:
            ##Test Case 17: nvme format command
            #call("./nvme format 0000.81:00.0 -n 1 -t 10 -l 1 -s 0 -i 0 -p 0 -m 0 -r",shell=True)
            pass#sleep(2)
    def test_case18(self,num):
        if num == 18:
            ##Test Case 18: nvme fw-activate command
            call("cd /home/wenzhong/nvme-cli && ./nvme fw-activate 0000:81:00.0 -s 1 -a 2",shell=True)
            sleep(2)
    def test_case19(self,num):
        if num == 19:
            ##Test Case 19: nvme fw-download command
            pass
    def test_case20(self,num):
        if num == 20:
            ##Test Case 20: nvme admin-passthru command
            call("cd /home/wenzhong/nvme-cli && ./nvme admin-passthru /dev/nvme0n1 -o 1 -f 1 -p 0 -R 1 -n 1 -m 1 -t 10 -2 1 -i /root/a -b -s -d -r ",shell=True)
            sleep(2)
    def test_case21(self,num):
        if num == 21:
            ##Test Case 21: nvme io-passthru command
            call("cd /home/wenzhong/nvme-cli && ./nvme io-passthru 0000:81:00.0 -o 1 -f 1 -p 0 -R 1 -n 1 -l 64 -m 1 -t 10 -2 1 -i /root/a -b -s -d -r -w ",shell=True)
            sleep(2)
    def test_case22(self,num):
        if num == 22:
            pass##Test Case 22: nvme security-send command NOTE:For Now,Just P4800 SUPPORT
    def test_case23(self,num):
        if num == 23:
            pass##Test Case 23: nvme security-recv command NOTE:For Now,Just P4800 SUPPORT
    def test_case24(self,num):
        if num == 24:
            pass##Test Case 25: nvme resv-register command NOTE:Not support
    def test_case25(self,num):
        if num == 25:
            pass##Test Case 26: nvme resv-release command  NoTE:Not Support 
    def test_case26(self,num):
        if num == 26:
            ##Test Case 27: nvme resv-report command
            call("cd /home/wenzhong/nvme-cli && ./nvme resv-report 0000:81:00.0",shell=True)
            sleep(2)
    def test_case27(self,num):
        if num == 27:
            ##Test Case 28: nvme dsm command
            call("cd /home/wenzhong/nvme-cli && ./nvme dsm -n 1 0000:81:00.0",shell=True)
            sleep(2)
    def test_case28(self,num):
        if num == 28:
            ##Test Case 29: nvme flush command
            call("cd /home/wenzhong/nvme-cli && ./nvme flush 0000:81:00.0 -n 1 ",shell=True)
            sleep(2)
    def test_case29(self,num):
        if num == 29:
            ##Test Case 30: nvme compare command P3700 Not Support
            #call("./nvme compare 0000:81:00.0 -s 0x1000 -c 0 -z 8 ",shell=True)
            sleep(2)
    def test_case30(self,num):
        if num == 30:
            ##Test Case 31: nvme write command
            call("cd /home/wenzhong/nvme-cli && echo "hello world" | nvme write /dev/nvme0n1 --data-size=520 --block-count=0 ",shell=True)
            #sleep(2)
            pass
    def test_case31(self,num):
        if num == 31:
            ##Test Case 32: nvme read command
            call("cd /home/wenzhong/nvme-cli && ./nvme read 0000:81:00.0 -s 0x0 -c 0x1 -z 1024",shell=True)
            sleep(2)
    def test_case32(self,num):
        if num == 32:
            ##Test Case 33: nvme write-zeroes command NOTE:Not SUPPOT in P3700 D3700
            pass
    def test_case33(self,num):
        if num == 33:
            ##Test Case 34: nvme write-uncor command 
            call("cd /home/wenzhong/nvme-cli && ./nvme write-uncor 0000:81:00.0 -n 1 -s 64 -c 1",shell=True);
            sleep(2)
    def test_case34(self,num):
        if num == 34:
            ##Test Case 35: nvme reset command
            call("cd /home/wenzhong/nvme-cli && ./nvme reset 0000:81:00.0",shell=True)
            sleep(2)
    def test_case35(self,num):
        if num == 35:
            ##Test Case 36: nvme subsystem-reset command
            call("cd /home/wenzhong/nvme-cli && ./nvme subsystem-reset",shell=True)
            sleep(2)
    def test_case36(self,num):
        if num == 36:
            ##Test Case 37: nvme show-regs command
            call("cd /home/wenzhong/nvme-cli && ./nvme show-regs 0000:81:00.0 -H",shell=True) 
            sleep(2)
    def test_case37(self,num):
        if num == 37:
            ##Test Case 38: nvme discover command
            call("cd /home/wenzhong/nvme-cli && ./nvme discover -t rdma -a 192.168.3.11 -s 4420",shell=True)
            sleep(2)
    def test_case38(self,num):
        if num == 38:
            ##Test Case 39: nvme connect-all command:
            #call("./nvme connect -t rdma -n "nqn.2016-06.io.spdk:cnode1" -a 192.168.3.11 -s 4420",shell=True)
            sleep(2)
            pass
    def test_case39(self,num):
        if num == 39:
            ##Test Case 40: nvme connect command
            #call("./nvme connect -t rdma -n "nqn.2016-06.io.spdk:cnode1" -a 192.168.3.11 -s 4420",shell=True)
            sleep(2)
            pass
    def test_case40(self,num):
        if num == 40:
            ##Test Case 41: nvme disconnect command
            #call("./nvme disconnect -n "nqn.2016-06.io.spdk:cnode4"",shell=True)
            sleep(2)
            pass
    def test_case41(self,num):
        if num == 41:
            ##Test Case 42: nvme gen-hostnqn command
            call("cd /home/wenzhong/nvme-cli ./nvme gen-hostnqn ",shell=True)
    def test_case42(self,num):
        if num == 42:
            ##Test Case 42: nvme recv-request command
            pass
