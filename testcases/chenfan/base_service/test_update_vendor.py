__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_vendor import ApiVendor
from data_structure.chenfan.base_service.data_vendor import UpdateVendorDate
from data_structure.chenfan.base_service.data_vendor import UpdateResVendorDate
from utils.restful import Restful

sys.path.insert(0, '..')


class TestUpdateVendor(unittest.TestCase):
    """
    供应商新增接口
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

    # def test_update_vendor_ok(self):
    #     """
    #     正常修改供应的必填信息，修改成功
    #     """
    #     # 1.准备必填的参数，有些非必选的参数可以不填
    #     vendorId ="476"
    #     cvenAddress = "测试"
    #     cvenHand = "17610225668"
    #     cvenPerson = "测试"
    #     vcCode = "01"
    #     vcId = "1"
    #     vcIdS = "1-01"
    #     venAbbName = "更新供应商12373"
    #     vendorCode = "12373"
    #     vendorName = "更新供应商12373"
    #     vensource = "招标渠道"
    #     factorylocation = "大店"
    #     vendorFiles = []
    #
    #     # 调用数据处理类，将参数合并到字典中
    #     body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
    #                               vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
    #                               vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)
    #
    #     # 2.调用接口
    #     response = self.api_vendor.put_update_vendor(body_data)
    #
    #     # 3.获取响应数据，判断状态码，并获取“data”
    #     message = "success"
    #     code = 200
    #     # 将返回解析后转换成dict的data数据
    #     # 若返回值不符合期望的状态码，message指明错误类型
    #     data_dec = self.restful.parse_response_text(response, code, message)
    #
    #     # 4.设置数据并在内部验证完整性
    #     UpdateResVendorDate(data_dec)
    #     print("test_update_vendor_ok pass")

    # def test_update_vendorName_ok(self):
    #     """
    #     修改供应商名称，修改成功
    #     """
    #     # 1.准备必填的参数，有些非必选的参数可以不填
    #     vendorId ="476"
    #     cvenAddress = "测试"
    #     cvenHand = "17610225668"
    #     cvenPerson = "测试"
    #     vcCode = "01"
    #     vcId = "1"
    #     vcIdS = "1-01"
    #     venAbbName = "更新供应商12373"
    #     vendorCode = "12373"
    #     vendorName = "更新供应商名称12373"
    #     vensource = "招标渠道"
    #     factorylocation = "大店"
    #     vendorFiles = []
    #
    #     # 调用数据处理类，将参数合并到字典中
    #     body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
    #                               vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
    #                               vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)
    #
    #     # 2.调用接口
    #     response = self.api_vendor.put_update_vendor(body_data)
    #
    #     # 3.获取响应数据，判断状态码，并获取“data”
    #     message = "success"
    #     code = 200
    #     # 将返回解析后转换成dict的data数据
    #     # 若返回值不符合期望的状态码，message指明错误类型
    #     data_dec = self.restful.parse_response_text(response, code, message)
    #
    #     # 4.设置数据并在内部验证完整性
    #     UpdateResVendorDate(data_dec)
    #     print("test_update_vendorName_ok pass")

    def test_null_vendorName_update_fail(self):
        """
        供应商名称不输入，修改供应商失败
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId ="476"
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = "更新供应商简称12373"
        vendorCode = "12373"
        vendorName = ""
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.put_update_vendor(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "供应商名称不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        UpdateResVendorDate(data_dec)
        print("test_null_vendorName_update_fail pass")

    # def test_update_venAbbName_ok(self):
    #     """
    #     修改供应商简称，修改成功
    #     """
    #     # 1.准备必填的参数，有些非必选的参数可以不填
    #     vendorId = "476"
    #     cvenAddress = "测试"
    #     cvenHand = "17610225668"
    #     cvenPerson = "测试"
    #     vcCode = "01"
    #     vcId = "1"
    #     vcIdS = "1-01"
    #     venAbbName = "更新供应商简称12373"
    #     vendorCode = "12373"
    #     vendorName = "更新供应商名称12373"
    #     vensource = "招标渠道"
    #     factorylocation = "大店"
    #     vendorFiles = []
    #
    #     # 调用数据处理类，将参数合并到字典中
    #     body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
    #                                  cvenPerson=cvenPerson, vcCode=vcCode,
    #                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
    #                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
    #                                  vendorFiles=vendorFiles)
    #
    #     # 2.调用接口
    #     response = self.api_vendor.put_update_vendor(body_data)
    #
    #     # 3.获取响应数据，判断状态码，并获取“data”
    #     message = "success"
    #     code = 200
    #     # 将返回解析后转换成dict的data数据
    #     # 若返回值不符合期望的状态码，message指明错误类型
    #     data_dec = self.restful.parse_response_text(response, code, message)
    #
    #     # 4.设置数据并在内部验证完整性
    #     UpdateResVendorDate(data_dec)
    #     print("test_update_venAbbName_ok pass")

    def test_null_venAbbName_update_fail(self):
        """
        不输入供应商简称，修改失败
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId = "476"
        cvenAddress = "测试地址修改"
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = ""
        vendorCode = "12373"
        vendorName = "更新供应商名称12373"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
                                     cvenPerson=cvenPerson, vcCode=vcCode,
                                     vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
                                     vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
                                     vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.put_update_vendor(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "供应商简称不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        UpdateResVendorDate(data_dec)
        print("test_null_cvenAddress_update_fail pass")

    # def test_update_vcCode_ok(self):
    #     """
    #     修改供应商所属分类，修改成功
    #     """
    #     # 1.准备必填的参数，有些非必选的参数可以不填
    #     vendorId = "476"
    #     cvenAddress = "测试"
    #     cvenHand = "17610225668"
    #     cvenPerson = "测试"
    #     vcCode = "03"
    #     vcId = "3"
    #     vcIdS = "3-03"
    #     venAbbName = "更新供应商简称12373"
    #     vendorCode = "12373"
    #     vendorName = "更新供应商名称12373"
    #     vensource = "招标渠道"
    #     factorylocation = "大店"
    #     vendorFiles = []
    #
    #     # 调用数据处理类，将参数合并到字典中
    #     body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
    #                                  cvenPerson=cvenPerson, vcCode=vcCode,
    #                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
    #                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
    #                                  vendorFiles=vendorFiles)
    #
    #     # 2.调用接口
    #     response = self.api_vendor.put_update_vendor(body_data)
    #
    #     # 3.获取响应数据，判断状态码，并获取“data”
    #     message = "success"
    #     code = 200
    #     # 将返回解析后转换成dict的data数据
    #     # 若返回值不符合期望的状态码，message指明错误类型
    #     data_dec = self.restful.parse_response_text(response, code, message)
    #
    #     # 4.设置数据并在内部验证完整性
    #     UpdateResVendorDate(data_dec)
    #     print("test_update_vcCode_ok pass")

    # def test_update_cvenPerson_ok(self):
    #     """
    #     修改联系人，修改成功
    #     """
    #     # 1.准备必填的参数，有些非必选的参数可以不填
    #     vendorId = "476"
    #     cvenAddress = "测试"
    #     cvenHand = "17610225668"
    #     cvenPerson = "测试修改联系人"
    #     vcCode = "03"
    #     vcId = "3"
    #     vcIdS = "3-03"
    #     venAbbName = "更新供应商简称12373"
    #     vendorCode = "12373"
    #     vendorName = "更新供应商名称12373"
    #     vensource = "招标渠道"
    #     factorylocation = "大店"
    #     vendorFiles = []
    #
    #     # 调用数据处理类，将参数合并到字典中
    #     body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
    #                                  cvenPerson=cvenPerson, vcCode=vcCode,
    #                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
    #                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
    #                                  vendorFiles=vendorFiles)
    #
    #     # 2.调用接口
    #     response = self.api_vendor.put_update_vendor(body_data)
    #
    #     # 3.获取响应数据，判断状态码，并获取“data”
    #     message = "success"
    #     code = 200
    #     # 将返回解析后转换成dict的data数据
    #     # 若返回值不符合期望的状态码，message指明错误类型
    #     data_dec = self.restful.parse_response_text(response, code, message)
    #
    #     # 4.设置数据并在内部验证完整性
    #     UpdateResVendorDate(data_dec)
    #     print("test_update_cvenPerson_ok pass")

    def test_null_cvenPerson_update_fail(self):
        """
        不输入联系人，修改失败
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId = "476"
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = ""
        vcCode = "03"
        vcId = "3"
        vcIdS = "3-03"
        venAbbName = "更新供应商简称12373"
        vendorCode = "12373"
        vendorName = "更新供应商名称12373"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
                                     cvenPerson=cvenPerson, vcCode=vcCode,
                                     vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
                                     vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
                                     vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.put_update_vendor(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "联系人不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        UpdateResVendorDate(data_dec)
        print("test_null_cvenPerson_update_fail pass")

    # def test_update_cvenHand_ok(self):
    #     """
    #     修改手机号，修改成功
    #     """
    #     # 1.准备必填的参数，有些非必选的参数可以不填
    #     vendorId = "476"
    #     cvenAddress = "测试"
    #     cvenHand = "17623456789"
    #     cvenPerson = "测试修改联系人"
    #     vcCode = "03"
    #     vcId = "3"
    #     vcIdS = "3-03"
    #     venAbbName = "更新供应商简称12373"
    #     vendorCode = "12373"
    #     vendorName = "更新供应商名称12373"
    #     vensource = "招标渠道"
    #     factorylocation = "大店"
    #     vendorFiles = []
    #
    #     # 调用数据处理类，将参数合并到字典中
    #     body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
    #                                  cvenPerson=cvenPerson, vcCode=vcCode,
    #                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
    #                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
    #                                  vendorFiles=vendorFiles)
    #
    #     # 2.调用接口
    #     response = self.api_vendor.put_update_vendor(body_data)
    #
    #     # 3.获取响应数据，判断状态码，并获取“data”
    #     message = "success"
    #     code = 200
    #     # 将返回解析后转换成dict的data数据
    #     # 若返回值不符合期望的状态码，message指明错误类型
    #     data_dec = self.restful.parse_response_text(response, code, message)
    #
    #     # 4.设置数据并在内部验证完整性
    #     UpdateResVendorDate(data_dec)
    #     print("test_update_cvenHand_ok pass")

    def test_null_cvenHand_update_fail(self):
        """
        不输入手机号码，修改失败
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId = "476"
        cvenAddress = "测试"
        cvenHand = ""
        cvenPerson = "修改联系人"
        vcCode = "03"
        vcId = "3"
        vcIdS = "3-03"
        venAbbName = "更新供应商简称12373"
        vendorCode = "12373"
        vendorName = "更新供应商名称12373"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
                                     cvenPerson=cvenPerson, vcCode=vcCode,
                                     vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
                                     vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
                                     vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.put_update_vendor(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "手机不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        UpdateResVendorDate(data_dec)
        print("test_null_cvenHand_update_fail pass")

    # def test_update_cvenAddress_ok(self):
    #     """
    #     修改地址，修改成功
    #     """
    #     # 1.准备必填的参数，有些非必选的参数可以不填
    #     vendorId = "476"
    #     cvenAddress = "修改测试地址"
    #     cvenHand = "17623456789"
    #     cvenPerson = "测试修改联系人"
    #     vcCode = "03"
    #     vcId = "3"
    #     vcIdS = "3-03"
    #     venAbbName = "更新供应商简称12373"
    #     vendorCode = "12373"
    #     vendorName = "更新供应商名称12373"
    #     vensource = "招标渠道"
    #     factorylocation = "大店"
    #     vendorFiles = []
    #
    #     # 调用数据处理类，将参数合并到字典中
    #     body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
    #                                  cvenPerson=cvenPerson, vcCode=vcCode,
    #                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
    #                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
    #                                  vendorFiles=vendorFiles)
    #
    #     # 2.调用接口
    #     response = self.api_vendor.put_update_vendor(body_data)
    #
    #     # 3.获取响应数据，判断状态码，并获取“data”
    #     message = "success"
    #     code = 200
    #     # 将返回解析后转换成dict的data数据
    #     # 若返回值不符合期望的状态码，message指明错误类型
    #     data_dec = self.restful.parse_response_text(response, code, message)
    #
    #     # 4.设置数据并在内部验证完整性
    #     UpdateResVendorDate(data_dec)
    #     print("test_update_cvenAddress_ok pass")

    def test_null_cvenAddress_update_fail(self):
        """
        不输入地址，修改失败
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        vendorId = "476"
        cvenAddress = ""
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = "更新供应商简称12373"
        vendorCode = "12373"
        vendorName = "更新供应商名称12373"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = UpdateVendorDate(vendorId=vendorId, cvenAddress=cvenAddress, cvenHand=cvenHand,
                                     cvenPerson=cvenPerson, vcCode=vcCode,
                                     vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName, factorylocation=factorylocation,
                                     vendorCode=vendorCode, vendorName=vendorName, vensource=vensource,
                                     vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.put_update_vendor(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "地址不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        UpdateResVendorDate(data_dec)
        print("test_null_cvenAddress_update_fail pass")