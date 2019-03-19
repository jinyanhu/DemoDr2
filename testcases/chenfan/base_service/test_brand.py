__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_brand import ApiBrand
from data_structure.chenfan.base_service.data_brand import *
from utils.restful import Restful

sys.path.insert(0, '..')


class TestBrand(unittest.TestCase):
    """
    品牌接口
    """
    def setUp(self):
        """
        测试类的构造方法
        该方法会在每个case运行前被调用一次
        """
        # 创建全局的接口调用类对象
        self.api_brand = ApiBrand()
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

    def test_get_brand_list_ok(self):
        """
        正常获取品牌列表
        """
        # 1.准备参数，有些非必选的参数可以不填

        # 2.调用接口
        response = self.api_brand.get_list()

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "获取品牌列表失败"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResBrandList(data_dec)

        print("test_get_brand_list_ok pass")

    def test_get_brand_list_by_code_ok(self):
        """
        通过品牌编码正常获取品牌列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        brand_code = "00001"
        body_data = DataBrandList(brandCode=brand_code)

        # 2.调用接口
        response = self.api_brand.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "获取品牌列表失败"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResBrandList(data_dec, body_data.get())

        print("test_get_brand_list_by_code_ok pass")

    def test_switch_brand_ok(self):
        """
        正常启用禁用品牌
        """
        # 1.准备参数，有些非必选的参数可以不填
        brand_id = "20"
        body_data = DataSwitchBrand(brand_id)

        # 2.调用接口
        response = self.api_brand.switch_brand(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "启用禁用品牌失败"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        data_req = dict()
        data_req["message"] = ""
        DataResSwitchBrand(data_dec)

        print("test_switch_brand_ok pass")