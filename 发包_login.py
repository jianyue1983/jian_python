import requests
import re
import urllib3
urllib3.disable_warnings() #禁止各种urllib3警告

class wireshark_login():
    def __init__(self):
        # 设置Session
        self.s=requests.session()
        # 设置请求头
        self.header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
        # 在使用Fiddler时进行请求，通过该代码忽略SSLError错误
        self.s.verify=False

    # 获取 authenticity_token
    def get_authenticity_token(self):
        login_url = "https://github.com/login"
        r = self.s.get(login_url, headers=self.headers)
        authenticity_token = re.findall('<input type="hidden" name="authenticity_token" value="(.+?)" />', r.text)
        print("authenticity_token：{}".format(authenticity_token))
        return authenticity_token[0]

    # 模拟登录，并返回 title
    def github_login(self, authenticity_token, username, password):
        session_url = "https://github.com/session"
        #构建body内容
        body = {
            "authenticity_token":authenticity_token,
            "commit":"Sign in",
            "login":username,
            "password":password,

        }
        r = self.s.post(session_url, headers = self.headers, data = body)
        title = re.findall('<title>(.+?)</title>',r.text)
        print("title：%s" %title[0])
        return title[0]

    # 通过 title 判断是否登录成功
    def is_login_success(self, title):
        if "GitHub" == title:
            return True
        else:
            return False

    if __name__ == '__main__':
        github = Github_Login()
        authenticity_token = github.get_authenticity_token()
        title = github.github_login(authenticity_token, username="用户名", password="密码")
        login_result = github.is_login_success(title)
        print(login_result)
