import json
from utils.database_util import Database
from utils.http_util import Http
from api_call.chenfan.base import BaseHttp
from api_call.chenfan.login.api_login import ApiLogin


class ApiRoute(BaseHttp):
    """
    esb加密接口
    """
    def __init__(self):

        BaseHttp.__init__(self)
        # self.database = Database("pymysql")
        # # self.api_login = ApiLogin()
        # # self.api_login.set_admin_login_header(self.header)  # 加登录header
        self.http = Http(self.header)  # http对象

    def esb_encrypt(self,body_data):
        """
        esb加密
        :return:
        """
        # 请求的地址
        url = self.url + "/encryptAndSign"
        # 请求esb接口得到返回值
        response = self.http.post(url=url,body=body_data)
        return response

    def route(self,body_data,headers):
        """
        短融ESB转发给E分期
        :return:
        """
        # 请求的地址
        url = "http://" + "192.168.0.104" + ":" + "9501" + "/bank/route"
        # 请求征信进件接口得到返回值
        response = self.http.post(url=url,body=body_data,headers=headers)
        return response

    def e_login(self,body_data):
        """
        登录E分期
        :return:
        """
        # 请求的地址
        url = "http://" + "14.17.122.160" + ":" + "19081" + "/login/doLogin"
        # 登录E分期
        response = self.http.post(url=url,body=body_data)
        return response

    def task_id(self,body_data,header):
        """
        获取taskid
        :return:
        """
        # 请求的地址
        url = "http://" + "14.17.122.160" + ":" + "19081" + "/loanOrder/workbench"
        # 获取taskid
        response = self.http.post(url=url,body=body_data,headers=header)
        return response

    def complete(self, body_data,header):
        """
        征信授权
        :return:
        """
        # 请求的地址
        url = "http://" + "14.17.122.160" + ":" + "19081" + "/tasks/complete"
        # 进行征信授权
        response = self.http.post(url=url, body=body_data,headers=header)
        return response

    # def delete_brand(self, sql):
    #     """
    #
    #     :param sql: sql语句
    #     :return:
    #     """
    #     self.database.update(sql=sql)
    # 测试代码提交11111111
