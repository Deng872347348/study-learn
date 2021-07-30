
"""
1、打开登录页面
2、输入用户名和密码
3、下载验证码图片到本地
4、登录成功
"""
import os,re,time
import requests
from utils.header import get_ua
from lxml import etree
import pytesseract
from PIL import Image



class GushiWen():
    def __init__(self):
        # 登录页地址
        self.login_url = "https://so.gushiwen.cn/user/login.aspx"
        # 验证码图片地址
        self.code_url = "https://so.gushiwen.cn/RandCode.ashx"
        # 个人中心收藏页面
        self.my_center_url = "https://so.gushiwen.cn/user/collect.aspx"
        self.code_img = "code.png"
        self.s = requests.session()
        self.headers = {"User-Agent":get_ua()}

    # 验证码识别或者输入
    def captcha(self,code_img_path):
        time.sleep(1)
        image = Image.open(code_img_path)
        text = pytesseract.image_to_string(image)
        length = len(text)
        print("机器识别的验证码长度：",length)
        if length > 4:
            try:
                text = text[:4]
            except:
                pass
            print("机器识别后的验证码为：" + text)
            command = input("请输入Y/y表示同意使用，按其他键自行重新输入：")
            if (command == "Y" or command == "y"):
                return text
            else:
                while True:
                    gs_code = input("请输入验证码:")
                    gs_code = gs_code.strip()
                    if gs_code:
                        return gs_code
                    else:
                        print("验证码不能为空，请重新输入！")
                        continue
        else:
            print("机器识别验证码长度小于4，直接输入验证码!")
            while True:
                gs_code = input("请输入验证码:")
                gs_code = gs_code.strip()
                if gs_code:
                    return gs_code
                else:
                    print("验证码不能为空，请重新输入！")
                    continue

    # 下载验证码
    def get_code(self):
        resp = self.s.get(self.code_url, headers= self.headers)
        if resp.status_code == 200:
            with open(self.code_img, "wb")as f:
                f.write(resp.content)
            code_img_path = os.path.abspath(self.code_img)
            print("验证码下载成功，即将自动打开，存放目录为：%s" % code_img_path)

            im = Image.open(code_img_path)
            im.show()


            # 先尝试机器识别验证码
            gs_code = self.captcha(code_img_path)
            return (gs_code,code_img_path)

        else:
            print("验证码获取失败，错误代码：",resp.status_code)
            return (False,False)

    # 用户输入完毕验证码后，删掉验证码
    def del_code(self,code_img_path):
        print("验证码输入完毕，删除验证码。")
        os.remove(code_img_path)

    # 获取两个值：viewstate和viewstategenerator
    def get_view(self):
        resp = self.s.get(self.login_url,headers=self.headers)
        html = etree.HTML(resp.text)
        viewstate = html.xpath('//div/input[@id="__VIEWSTATE"]/@value')
        viewstategenerator = html.xpath('//div/input[@id="__VIEWSTATEGENERATOR"]/@value')
        return (viewstate,viewstategenerator)

    def login(self, account_num, pwd):
        gs_code,code_img_path = self.get_code()
        viewstate, viewstategenerator = self.get_view()
        data = {
            "__VIEWSTATE": viewstate,
            "__VIEWSTATEGENERATOR":viewstategenerator,
            "from": "",
            "email": account_num,
            "pwd": pwd,
            "code": gs_code,
            "denglu": "登录"
        }
        if gs_code:
            resp = self.s.post(self.login_url, data=data, headers= self.headers)

            self.del_code(code_img_path)
            if "登录失败，您输入的账号错误或不存在" in resp.text:
                print("登录失败，您输入的账号错误或不存在！")
                self.main()
            elif "提交失败，您输入的验证码有误" in resp.text:
                print("提交失败，您输入的验证码有误，将会重新获取验证码！")
                self.login(account_num, pwd)
            elif "登录失败，您输入的密码错误" in resp.text:
                print("登录失败，您输入的密码错误！")
                self.main()
            else:
                if resp.status_code == 200:
                    my_resp = self.s.get(self.my_center_url,headers=self.headers)
                    root = etree.HTML(my_resp.text)
                    try:
                        res = []
                        # 作者
                        authors = root.xpath('//div[@id="mainSearch"]/div[2]/div/div/a/span/text()')
                        # 标题
                        titles = root.xpath('//div[@id="mainSearch"]/div[2]/div/div/a/text()')
                        for i in zip(titles,authors):
                            res.append("".join(i))
                        # 去掉空格
                        res = [i.replace(" ","") for i in res]
                        # ['沁园春·记上层楼-陈人杰', '重赠卢谌-刘琨', '莲藕花叶图-吴师道']
                        print("我的收藏：",res)
                    except:
                        print("暂无收藏！")
                    self.close()

    # 退出
    def close(self):
        time.sleep(2)
        print("退出网页...")
        self.s.get("http://so.gushiwen.cn/user/collect.aspx?type=s", headers=self.headers)

    # 入口
    def main(self):
        while True:
            account_num = input("请输入账号(邮箱/手机号)：").strip()
            # 判断邮箱格式和手机号格式
            phone_patt = re.compile(r"^1[3-9]\d{9}$")
            email_patt = re.compile(r"^[\w\-]+@[0-9a-zA-Z]+\.[a-zA-Z]+\.?[a-zA-Z]+$")

            if account_num:
                p = phone_patt.findall(account_num)
                e = email_patt.findall(account_num)
                if p or e:
                    break
                else:
                    print("手机号或邮箱格式不正确！")
                    continue
            else:
                print("账号不能为空！")
                continue
        while True:
            pwd = input("请输入密码(6-20位)：").strip()
            pw_patt = re.compile(r"^\w{6,20}$")
            if pwd:
                pw = pw_patt.findall(pwd)
                if not pw:
                    print("密码长度为6-20字符！")
                    continue

                else:
                    break
            else:
                print("密码不能为空！")
                continue
        self.login(account_num,pwd)

if __name__ == '__main__':
    gs = GushiWen()
    gs.main()