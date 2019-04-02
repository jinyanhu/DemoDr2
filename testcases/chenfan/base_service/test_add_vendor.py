__author__ = 'zzh'

import sys
import unittest  # 单元测试框架
import random

from api_call.chenfan.base_service.api_vendor import ApiVendor
from data_structure.chenfan.base_service.data_vendor import DataVendorAdd
from data_structure.chenfan.base_service.data_vendor import DataResVendorAdd
from utils.restful import Restful

sys.path.insert(0, '..')


class TestAddVendor(unittest.TestCase):
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

    def test_add_vendor_ok(self):
        """
        输入所有必填项，正常新增供应商
        """
        # 1.准备必填的参数，有些非必选的参数可以不填
        """
        获取随机的5位纯数字当做供应商编码
        """
        str = ""
        for i in range(5):
            ch = chr(random.randrange(ord('0'),ord('9') + 1))
            str += ch
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = str
        vendorCode = str
        vendorName = str
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)
        """sql = "DELETE FROM vendor WHERE vendor_code = '01233'"
        self.api_vendor.delete_vendor(sql=sql)
        """

        print("test_add_vendor_ok pass")

    def test_add_vendor_no_vendorCode_fail(self):
        """
        不输入供应商编码，新增供应商失败
        """
        # 1.准备参数，供应商编码不传
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = "测试01231"
        vendorCode = ""
        vendorName = "测试01231"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "供应商编码不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_add_vendor_no_vendorCode_fail pass")

    def test_add_vendor_no_vendorName_fail(self):
        """
        不输入供应商名称，新增供应商失败
        """
        # 1.准备参数，供应商名称不传
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = "测试01233"
        vendorCode = "01233"
        vendorName = ""
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "供应商名称不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_add_vendor_no_vendorName_fail pass")

    def test_add_vendor_no_venAbbName_fail(self):
        """
        不输入供应商名称，新增供应商失败
        """
        # 1.准备参数，供应商名称不传
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = ""
        vendorCode = "01233"
        vendorName = "测试01233"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "供应商名称不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_add_vendor_no_venAbbName_fail pass")

    def test_add_vendor_no_vcCode_fail(self):
        """
        不输入供应商所属分类，新增供应商失败
        """
        # 1.准备参数，供应商所属分类不传
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = ""
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = ""
        vendorCode = "01233"
        vendorName = "测试01233"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "供应商分类编码不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_add_vendor_no_vcCode_fail pass")

    def test_add_vendor_cvenPerson_fail(self):
        """
        不输入联系人，新增供应商失败
        """
        # 1.准备参数，联系人不传
        cvenAddress = "测试"
        cvenHand = "17610225668"
        cvenPerson = ""
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = "测试01233"
        vendorCode = "01233"
        vendorName = "测试01233"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "联系人不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_add_vendor_cvenPerson_fail pass")

    def test_add_vendor_cvenHand_fail(self):
        """
        不输入手机，新增供应商失败
        """
        # 1.准备参数，联系人不传
        cvenAddress = "测试"
        cvenHand = ""
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = "测试01233"
        vendorCode = "01233"
        vendorName = "测试01233"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "手机不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)

        print("test_add_vendor_cvenPerson_fail pass")

    def test_add_vendor_cvenAddress_fail(self):
        """
        不输入地址1，新增供应商失败
        """
        # 1.准备参数，地址1不传
        cvenAddress = ""
        cvenHand = "17610225668"
        cvenPerson = "测试"
        vcCode = "01"
        vcId = "1"
        vcIdS = "1-01"
        venAbbName = "测试01233"
        vendorCode = "01233"
        vendorName = "测试01233"
        vensource = "招标渠道"
        factorylocation = "大店"
        vendorFiles = []

        # 调用数据处理类，将参数合并到字典中
        body_data = DataVendorAdd(cvenAddress=cvenAddress, cvenHand=cvenHand, cvenPerson=cvenPerson, vcCode=vcCode,
                                  vcId=vcId, vcIdS=vcIdS, venAbbName=venAbbName,factorylocation=factorylocation,
                                  vendorCode=vendorCode, vendorName=vendorName, vensource=vensource, vendorFiles=vendorFiles)

        # 2.调用接口
        response = self.api_vendor.post(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "地址不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResVendorAdd(data_dec)
        print("test_add_vendor_cvenPerson_fail pass")
