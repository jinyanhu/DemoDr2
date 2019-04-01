__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_vendor import ApiVendor
from data_structure.chenfan.base_service.data_vendor import DataSwitchBanVendor
from data_structure.chenfan.base_service.data_vendor import DataResSwitchBanVendor
from utils.restful import Restful

sys.path.insert(0, '..')


class TestVendorState(unittest.TestCase):
    """
    供应商接口
    """
    def setUp(self):
        """
        测试类的构造方法
        该方法会在每个case运行前被调用一次
        """
        # 创建全局的接口调用类对象
        self.api_vendor = ApiVendor()
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

    def test_start_vendor_ok(self):
        """
        启用供应商
        """
        # 1.准备参数，有些非必选的参数可以不填
        vendorId = 1

        # 2.调用接口
        body_data = DataSwitchBanVendor(vendorId=vendorId)
        response = self.api_vendor.put(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResSwitchBanVendor(data_dec)

        print("test_start_vendor_ok pass")

    def test_stop_vendor_ok(self):
        """
        禁用供应商
        """
        # 1.准备参数，有些非必选的参数可以不填
        vendorId = 2

        # 2.调用接口
        body_data = DataSwitchBanVendor(vendorId=vendorId)
        response = self.api_vendor.put(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResSwitchBanVendor(data_dec)

        print("test_start_vendor_ok pass")

    def test_start_vendor_fail(self):
        """
        不选择供应商，启用供应商失败
        """
        # 1.准备参数，有些非必选的参数可以不填
        vendorId = 1000263

        # 2.调用接口
        body_data = DataSwitchBanVendor(vendorId=vendorId)
        response = self.api_vendor.put(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "启用供应商失败"
        code = 401
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResSwitchBanVendor(data_dec)

        print("test_start_vendor_ok pass")

    def test_stop_vendor_fail(self):
        """
        不选择供应商，禁用供应商失败
        """
        # 1.准备参数，有些非必选的参数可以不填
        vendorId = 1000263

        # 2.调用接口
        body_data = DataSwitchBanVendor(vendorId=vendorId)
        response = self.api_vendor.put(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "禁用供应商失败"
        code = 401
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResSwitchBanVendor(data_dec)

        print("test_start_vendor_ok pass")
