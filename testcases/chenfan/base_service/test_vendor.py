__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_vendor import ApiVendor
from data_structure.chenfan.base_service.data_vendor import DataVendorList
from data_structure.chenfan.base_service.data_vendor import DataResVendorAdd
from data_structure.chenfan.base_service.data_vendor import DataResVendorList
from utils.restful import Restful

sys.path.insert(0, '..')


class TestVendor(unittest.TestCase):
    """
    供应商列表接口
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

    def test_get_vendor_list_ok(self):
        """
        正常获取供应商列表
        """
        # 1.准备参数，有些非必选的参数可以不填

        # 2.调用接口
        response = self.api_vendor.get_list()

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorList(data_dec)

        print("test_get_vendor_list_ok pass")

    def test_get_vendor_code_list_ok(self):
        """
        根据供应商编码获取供应商列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        vendorCode = "01231"

        # 2.调用接口
        body_data = DataVendorList(vendorCode=vendorCode)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorList(data_dec)

        print("test_get_vendor_code_list_ok pass")

    def test_get_vendor_venAbbName_list_ok(self):
        """
        根据供应商简称获取供应商列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        venAbbName = "RUMI"

        # 2.调用接口
        body_data = DataVendorList(venAbbName=venAbbName)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorList(data_dec)

        print("test_get_vendor_venAbbName_list_ok pass")

    def test_get_vendor_state_list_ok(self):
        """
        根据供应商启用状态获取供应商列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        state = "1"

        # 2.调用接口
        body_data = DataVendorList(state=state)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorList(data_dec)

        print("test_get_vendor_state_list_ok pass")

    def test_get_vendor_ventype_list_ok(self):
        """
        根据供应商类型获取供应商列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        ventype = "品牌公司，有生产配套"

        # 2.调用接口
        body_data = DataVendorList(ventype=ventype)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorList(data_dec)

        print("test_get_vendor_ventype_list_ok pass")

    def test_get_vendor_vensource_list_ok(self):
        """
        根据供应商来源获取供应商列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        vensource = "招标渠道"

        # 2.调用接口
        body_data = DataVendorList(vensource=vensource)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorList(data_dec)

        print("test_get_vendor_vensource_list_ok pass")

    def test_get_vendor_list_fail(self):
        """
        输入不存在的供应商编码，获取不到列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        vendorCode = "987650"

        # 2.调用接口
        body_data = DataVendorList(vendorCode=vendorCode)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "获取供应商列表失败"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_get_vendor_list_fail pass")

    def test_get_vendor_category_list_OK(self):
        """
        输入产品类目，获取列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        category = "梭织"

        # 2.调用接口
        body_data = DataVendorList(category=category)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)
        print("test_get_vendor_category_list_OK pass")

    def test_get_vendor_factoryGrade_list_OK(self):
        """
        输入工厂等级，获取列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        factoryGrade = "A"

        # 2.调用接口
        body_data = DataVendorList(factoryGrade=factoryGrade)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_get_vendor_category_list_OK pass")

    def test_get_vendor_coreproduct_list_OK(self):
        """
        输入供应商核心产品，获取列表
        """
        # 1.准备参数，有些非必选的参数可以不填
        coreproduct = "连衣裙"

        # 2.调用接口
        body_data = DataVendorList(coreproduct=coreproduct)
        response = self.api_vendor.get_list(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_get_vendor_coreproduct_list_OK pass")

