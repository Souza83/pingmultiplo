import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando ip: ', ip)
        print('-' * 65)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 65)
        time.sleep(5)