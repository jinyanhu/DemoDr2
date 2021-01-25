
import sys
import unittest  # 单元测试框架
import time
from urllib import parse

from api_call.chenfan.base_service.api_route import ApiRoute
from data_structure.chenfan.base_service.data_esb import DataRouteEsb
from data_structure.chenfan.base_service.data_esb import DataResEsb
from utils.restful import Restful
from testcases.chenfan.base_service.test_esb import TestEsbReturn

sys.path.insert(0, '..')


class TestICBCComplete(unittest.TestCase):
    """
    ICBC征信授权
    """
    def setUp(self):
        """
        测试类的构造方法
        该方法会在每个case运行前被调用一次
        """
        # 创建全局的接口调用类对象
        self.api_route = ApiRoute()
        self.test_esb = TestEsbReturn()
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

    def test_login(self):
        """
        登录E分期
        """

        body_data = {

                "account": "360209841",
                "LoginAgent": "WEB",
                "password": "BErAgCECPtRUvBWme5yrCd0dBVW56c0rAeSgXD4Uqil+qfaOlC/7LL8kQA8AqJZBaUHrl2CbujpI51bqZ8FWEwwEyeJGVLTPk3fdG/KvIF3C9VlWP0VyQSZYyDJdUUeZzD8yUmkfIhIMd80gn9KMNjd3Du526aKgaNpqXE6lIEw="

        }
        # 2.调用接口
        response = self.api_route.e_login(body_data=body_data)
        # 3.获取响应数据，判断状态码，并获取“data”
        msg = "success"
        code = 0
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, msg)


        # 4.设置数据并在内部验证完整性
        DataResEsb(data_dec)
        print("login pass")
        return data_dec

    # 获取taskid
    def test_taskid(self):
        token_data = self.test_login()
        token = token_data["data"]["token"]
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Bearer" + " " + "{}".format(token)
        }
        orderno = self.test_esb.test_route()
        FomData = {

                # "fuzzyParam": "vx001002001803293333848854528",
                "fuzzyParam": orderno,
                "checkType": "0"
        }
        data = parse.urlencode(FomData)
        response = self.api_route.task_id(body_data=data,header=header)
        # 返回值转化成json格式
        response_json=response.json()
        print(response_json)




