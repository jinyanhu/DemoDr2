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

    # def delete_brand(self, sql):
    #     """
    #
    #     :param sql: sql语句
    #     :return:
    #     """
    #     self.database.update(sql=sql)
    # 测试代码提交
