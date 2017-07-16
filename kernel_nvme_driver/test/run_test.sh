fio ./randread_1qd > /home/kernel_log/randread_1qd.log
sleep 5
fio ./randread_4qd >/home/kernel_log/randread_4qd.log
sleep 5
fio ./randread_16qd >/home/kernel_log/randread_16qd.log
sleep 5

'''
fio ./randwrite_1qd >./log/randwrite_1qd.log
sleep 5
fio ./randwrite_4qd >./log/randwrite_4qd.log
sleep 5
fio ./randwrite_16qd >./log/randwrite_16qd.log
sleep 5

fio ./randrw_1qd >./log/randrw_1qd.log
sleep 5
fio ./randrw_4qd >./log/randrw_4qd.log
sleep 5
fio ./randrw_16qd >./log/randrw_16qd.log
sleep 5
'''
