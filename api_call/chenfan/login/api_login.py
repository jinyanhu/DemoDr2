__author__ = 'Administrator'

"""
登录
"""
import json
from utils.http_util import Http
from api_call.chenfan.base import BaseHttp
from utils.conf import MyCfg


class ApiLogin(BaseHttp):
    def __init__(self):
        """
        初始化方法
        各个接口方法封装中需要的公共内容，可以统一写在这里
        """
        BaseHttp.__init__(self)                 # 父类初始化
        self.http = Http(self.header)  # http对象
        self.conf = MyCfg("chenfan.ini")
        self.conf.set_section("user_info")

    # ####################### 以下的每个方法，对应封装一个接口的调用过程 ################### #
    def post(self, body_data):
        """
        登录接口
        """
        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        body_data = body_data.get()
        body_data["codeToken"] = self.get_code_token()

        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉
        self.header["dataType"] = body_data["dataType"]

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/user_login"
        response = self.http.post(url, body=body_data, headers=self.header)       # post方法

        # 返回响应数据
        return response

    def get_code_token(self):
        """
        获取验证码，返回codeToken
        :return:
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/verify_code"
        response = self.http.get(url)  # post方法
        data = response.text
        data_json = json.loads(data)
        code_token = data_json["obj"]["token"]

        # 返回响应数据
        return code_token

    def admin_login(self):
        """
        企业管理员账号zzh登录，返回token和企业类型字典
        :return:
        """
        self.header["dataType"] = "qy"

        login_dict = dict()
        login_dict["data_type"] = "qy"

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        body_data = dict()
        body_data["code"] = self.conf.get("admin_code")
        body_data["dataType"] = self.conf.get("admin_data_type")
        body_data["password"] = self.conf.get("admin_password")
        body_data["userName"] = self.conf.get("admin_user_name")
        body_data["codeToken"] = self.get_code_token()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/user_login"
        response = self.http.post(url, body=body_data, headers=self.header)  # post方法

        cookie = response.headers["set-cookie"]
        data = response.text
        data_json = json.loads(data)
        login_dict["token"] = data_json["obj"]["token"]
        login_dict["user_id"] = data_json["obj"]["userId"]
        login_dict["Cookie"] = cookie + ";token=" + data_json["obj"]["token"]

        return login_dict

    def set_admin_login_header(self, headers):
        """
        设置企业管理员登录header
        :return:
        """
        login_dict = self.admin_login()
        headers["Authorization"] = login_dict["token"]
        headers["dataType"] = login_dict["data_type"]
        headers["Cookie"] = login_dict["Cookie"]


if __name__ == "__main__":
    # 该区域的代码只在run当前文件时执行
    # 可以在此简单测试下封装的接口调用方法
    pass



