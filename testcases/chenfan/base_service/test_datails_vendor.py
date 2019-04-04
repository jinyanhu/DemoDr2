__author__ = 'zzh'

import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_vendor import ApiVendor
from data_structure.chenfan.base_service.data_vendor import DataVendorInfo
from data_structure.chenfan.base_service.data_vendor import DataResVendorInfo
from utils.restful import Restful

sys.path.insert(0, '..')


class TestDetailsVendor(unittest.TestCase):
    """
    供应商查看详情接口
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

    def test_details_vendor_ok(self):
        """
        输入供应商ID，获取供应商详情成功
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId = 1
        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorInfo(vendorId=vendorId)

        # 2.调用接口
        response = self.api_vendor.get_vendor_details(body_data)
        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        body_data = body_data.get()
        body_data["vendorName"] = "RUMI"
        body_data["vendorCode"] = "00005"
        body_data["venAbbName"] = "RUMI"
        # 4.设置数据并在内部验证完整性
        DataResVendorInfo(data_dec, body_data)
        print("test_details_vendor_ok pass")

    def test_null_vendor_id_ok(self):
        """
        不输入供应商ID，获取供应商详情失败
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId = ""
        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorInfo(vendorId=vendorId)

        # 2.调用接口
        response = self.api_vendor.get_vendor_details(body_data)
        # 3.获取响应数据，判断状态码，并获取“data”
        message = "ID不可为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorInfo(data_dec)
        print("test_null_vendor_id_ok pass")

    def test_error_vendor_id_ok(self):
        """
        供应商id不存在，获取供应商详情失败
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId = 5444
        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorInfo(vendorId=vendorId)

        # 2.调用接口
        response = self.api_vendor.get_vendor_details(body_data)
        # 3.获取响应数据，判断状态码，并获取“data”
        message = "ID不存在"
        code = 500
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message)

        # 4.设置数据并在内部验证完整性
        # DataResVendorInfo(data_dec)
        print("test_error_vendor_id_ok pass")