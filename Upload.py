import sys
from trend_api import *
from API1226 import *
if len(sys.argv) < 2: 
    print 'Need argv. you can use --help to show the help cmd'
    sys.exit()
    
if sys.argv[1].startswith('--'): 
    option = sys.argv[1][2:] 

    if option == 'help': 
        print ''' 
Options include: 
--help  :  Display this help
--vhost :  Upload Vhost test result
--nvmf  :  Upload nvmf-target test result
--nvme  :  Upload the nvme-driver test result
--trend :  Upload the test result to the web 
--detail:  Upload the detail result to the web
--all   :  Upload all result include detail and trend
Example:
    Use cmd: "python trend.py --nvmf --trend" Upload nvmf-target trend test result
    Use cmd: "python trend --vhost --detail"  Upload vhost detail test result
'''
    else: 
        print "Unknown option: Use --help to get the option help"
    sys.exit() 
    if len(sys.argv) > 2:
        select = sys.argv[2][2:]
        print select
# fetch sys.argv[1] but without the first two characters 
        if option == 'nvmf':
            if select == 'all':
                print 'nvmf-target all reault upload success!'
            if select == 'trend':
                draw_spdk_nvmf_target_trend_result()
                print 'nvmf-target trend result upload success!'
            if select == 'detail':
                print 'nvmf-target detail upload success!'
        if option == 'nvme':
            if select == 'all':
                print 'nvme all'
            if select == 'trend':
                print 'nvme trend'
            if select == 'detail':
                print 'nvme detail'
        if option == 'vhost':
            if select == 'all':
                print 'vhost all'
            if select == 'trend':
                print 'vhost trend'
            if select == 'detail':
                print 'detail detail'
