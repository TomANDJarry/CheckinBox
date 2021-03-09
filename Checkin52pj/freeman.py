import requests,os
import time
email = ""
passwd = ""
def get_sign(url):
    s = requests.Session()
    email = os.environ.get('freeman_email')
    passwd = os.environ.get('freeman_passwd')
    headers = {
        "Content-Length": "46",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin" : "http://freeperson.xyz",
        "Referer" : "http://freeperson.xyz/auth/login"
    }
    data = {
        "email":email,
        "passwd":passwd,
    }
    url1 = url + 'auth/login'
    url2 = url + 'user/checkin'
    url3 = url + 'user/logout'
    try:
        rep = s.post(url=url1,data =data,verify=False,headers=headers, allow_redirects=False)
        print(rep.text)
        signrep = s.post(url=url2,verify=False, allow_redirects=False)
        print(signrep.text)
        loginoutrep = s.get(url=url3, verify=False,allow_redirects=False)
        print(loginoutrep.text)
    except Exception as e:
        print(e)
        print("登陆失败！")
        pass
if __name__ == '__main__':
    get_sign("http://freeperson.xyz/")
