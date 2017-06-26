from subprocess import call,check_call
#l=[]
#dev = call("lsblk|awk '{print $1}'|grep nvme",shell=True,stdin=l)
#print dev
#dev = str(dev),l;
#rint dev[0:-1];
#print dev.split("n");
#target_list = [str(x) for x in dev[0:-1].split('\n')]
#print target_list
#print type(dev)



#for dev1 in dev:
    #check_call('nvme disconnect -d %s'%dev1,shell=True);
for i in range(0,64):
    dev = 'nvme%sn1'%i
    print dev
    call('nvme disconnect -d %s'%dev,shell=True);
