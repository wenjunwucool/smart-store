import sys

if len(sys.argv) < 2: 
    print 'Need argv. you can use --help to show the help cmd'
    sys.exit()
    
if sys.argv[1].startswith('--'): 
    option = sys.argv[1][2:] 

    if option == 'help': 
        print ''' 
Options include: 
--help  :  Display this help
--result:  Only get the test result not Upload
--file  :  Get result from fio log file
--dir   :  Get result from fio log dir
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
    if option == 'file'
        print 'get result from fio log file success!'
    if option == 'dir'
        print 'get result from '
    else: 
        print "Unknown option: Use --help to get the option help"
    sys.exit() 
    if len(sys.argv) > 2:
        select = sys.argv[2][2:]
        print select
# fetch sys.argv[1] but without the first two characters 
        if option == 'nvmf':
            if select == 'all':
                print 'nvmf all'
            if select == 'trend':
                print 'nvmf trend'
            if select == 'detail':
                print 'nvmf detail'
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
