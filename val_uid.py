import requests 
url = "http://IP/_session/sess_"

def check_login(s_i):
    res = requests.get(url+s_i)
    if '1' in res.text:
        print(s_i + ' :loggedin')
with open('sessions','r') as file_sess:
    sess = [i.replace('\n','') for i in file_sess.readlines()]
    sess.reverse()

    for i in sess:
        check_login(i)
