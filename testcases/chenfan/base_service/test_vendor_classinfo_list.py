__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_vendor import ApiVendor
from data_structure.chenfan.base_service.data_vendor import DataVendorClassInfoList
from data_structure.chenfan.base_service.data_vendor import DataResVendorClassInfoList
from utils.restful import Restful

sys.path.insert(0, '..')


class TestVendorClassInfoList(unittest.TestCase):
    """
    供应商分类接口
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

    def test_get_vendor_class_info_list_ok(self):
        """
        正常获取供应商分类编码列表
        """
        # 1.准备参数，有些非必选的参数可以不填

        # 2.调用接口
        response = self.api_vendor.get_vendor_class_info_list()

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResVendorClassInfoList(data_dec)

        print("test_get_vendor_class_info_list_ok pass")

