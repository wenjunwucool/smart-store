#!/bin/bash

for i in $(seq 105000)
do
	nvme disconnect -n "nqn.2016-06.io.spdk:cnode$i"
done

#for i in $(seq 128)
#do
#	nvme connect -t rdma -n "nqn.2016-06.io.spdk:cnode$i" -a 192.168.3.11 -s 4420
#done
