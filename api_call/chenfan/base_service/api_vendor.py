__author__ = 'Administrator'

"""
供应商
"""
import json
from utils.http_util import Http
from api_call.chenfan.base import BaseHttp
from api_call.chenfan.login.api_login import ApiLogin


class ApiAddVendor(BaseHttp):
    def __init__(self):
        """
        供应商创建请求接口
        初始化方法
        各个接口方法封装中需要的公共内容，可以统一写在这里
        """
        BaseHttp.__init__(self)                 # 父类初始化
        self.api_login = ApiLogin()
        self.api_login.set_admin_login_header(self.header)  # 加登录header
        self.http = Http(self.header)  # http对象

    # ####################### 以下的每个方法，对应封装一个接口的调用过程 ################### #

    def post(self, body_data=None):
        """
        新增供应商
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/vendor/add"
        response = self.http.post(url=url, body=body_data, headers=self.header)       # post方法

        # 返回响应数据
        return response


class ApiVendor(BaseHttp):
    def __init__(self):
        """
        供应商创建请求接口
        初始化方法
        各个接口方法封装中需要的公共内容，可以统一写在这里
        """
        BaseHttp.__init__(self)  # 父类初始化
        self.api_login = ApiLogin()
        self.api_login.set_admin_login_header(self.header)  # 加登录header
        self.http = Http(self.header)  # http对象

    def get_list(self, body_data=None):
        """
        获取供应商列表
        """
        # 用字典字段赋值的方式，对header某个需要变更的字段赋值
        # tag是预留给伪接口的标志，若不使用伪接口，tag可以删掉

        # 将一个dict数据参数传入，直接设置为body数据，转换为json
        if body_data:
            body_data = body_data.get()

        # 调用对应http方法，加入body参数，发送请求
        url = self.url + "/chenfan_base/vendor/getList"
        response = self.http.get(url, params=body_data)  # get方法

        # 返回响应数据
        return response


if __name__ == "__main__":
    # 该区域的代码只在run当前文件时执行
    # 可以在此简单测试下封装的接口调用方法
    pass



