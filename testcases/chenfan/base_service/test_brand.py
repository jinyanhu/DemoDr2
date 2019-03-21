

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_brand import ApiBrand
from data_structure.chenfan.base_service.data_brand import DataBrand
from data_structure.chenfan.base_service.data_brand import DataResBrand
from data_structure.chenfan.base_service.data_brand import DataResBrandFailure
from utils.restful import Restful

sys.path.insert(0, '..')


class TestBrand(unittest.TestCase):
    """
    品牌列表接口
    """
    def setUp(self):
        # 实例化ApiBrand类
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
        :return:
        """
        response = self.api_brand.get_brand_list()
        code = 200
        message = "获取品牌列表失败"
        # 转换response的类型为字典类型，若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言data_dec中的数据正确性
        DataResBrand(data_dec)

        print("test_get_brand_list_ok pass")

    def test_get_code_brand_list(self):
        """
        根据品牌编码获取品牌列表
        :return:
        """
        # 准备请求参数
        brandCode = "00001"
        body_data = DataBrand(brandCode=brandCode)
        # 调用接口
        response = self.api_brand.get_code_brand_list(body_data)
        code = 200
        message = "获取品牌列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResBrand(data_dec)
        print("test_get_code_brand_list pass")

    def test_get_code_brand_list_failure(self):
        """
        根据不存在的品牌编码获取品牌列表
        :return:
        """
        # 准备请求参数
        brandCode = "99999"
        body_data = DataBrand(brandCode=brandCode)
        # 调用接口
        response = self.api_brand.get_code_brand_list_failure(body_data)
        code = 200
        message = "获取品牌列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResBrandFailure(data_dec)
        print("test_get_code_brand_list_failure pass")

    def test_get_name_brand_list(self):
        """
        根据品牌名称获取品牌列表
        :return:
        """
        brandName = "Chinstudio"
        body_data = DataBrand(brandName=brandName)
        response = self.api_brand.get_name_brand_list(body_data)
        code = 200
        message = "获取品牌列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        DataResBrand(data_dec)
        print("test_get_name_brand_list pass")

    def test_get_name_brand_list_nothing(self):
        """
        根据不存在的品牌名称获取品牌列表
        :return:
        """
        brandName = "ABCDEF"
        body_data = DataBrand(brandName=brandName)
        response = self.api_brand.get_name_brand_list_nothing(body_data)
        code = 200
        message = "获取品牌列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        DataResBrandFailure(data_dec)
        print("test_get_name_brand_list_nothing pass")

    def test_get_state_brand_list_enable(self):
        """
        根据品牌启用状态获取品牌列表
        :return:
        """
        state = 1
        body_data = DataBrand(state=state)
        response = self.api_brand.get_state_brand_list_enable(body_data)
        code = 200
        message = "获取品牌列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        DataResBrand(data_dec)
        print("test_get_state_brand_list_enable pass")

    def test_get_state_brand_list_disable(self):
        """
        根据品牌启用状态获取品牌列表
        :return:
        """
        state = 0
        body_data = DataBrand(state=state)
        response = self.api_brand.get_state_brand_list_disable(body_data)
        code = 200
        message = "获取品牌列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        DataResBrand(data_dec)
        print("test_get_state_brand_list_disable pass")

