__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.login.api_login import ApiLogin
from data_structure.chenfan.login.data_login import DataLogin
from data_structure.chenfan.login.data_login import DataResLogin
from utils.restful import Restful

sys.path.insert(0, '..')


class TestLogin(unittest.TestCase):
    """
    登录接口
    """
    def setUp(self):
        """
        测试类的构造方法
        该方法会在每个case运行前被调用一次
        """
        # 创建全局的接口调用类对象
        self.api_login = ApiLogin()
        # 赋值self的其他字段
        self.restful = Restful()
        # 资源列表，用以回收资源
        self.service_id_list = list()

    def tearDown(self):
        """
        测试类的析构方法
        该方法会在每个case运行后被调用一次
        """
        pass

    def test_login_ok(self):
        """
        正常登录
        """
        # 1.准备参数，有些非必选的参数可以不填
        code = "zhihe666"
        dataType = "qy"
        password = "Chenfan123"
        userName = "zhangzhihe"
        body_data = DataLogin(userName=userName, password=password, dataType=dataType, code=code)

        # 2.调用接口
        response = self.api_login.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "登录失败"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResLogin(data_dec, body_data.get())

        print("test_login_ok pass")
