__author__ = 'zzh'

import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_priceJust import ApiPriceJust
from data_structure.chenfan.base_service.data_priceJust import ExportPrinceJust
from utils.restful import Restful

sys.path.insert(0, '..')


class TestExportPriceJust(unittest.TestCase):
    """
    存货调价单导出接口
    """
    def setUp(self):
        """
        测试类的构造方法
        该方法会在每个case运行前被调用一次
        """
        # 创建全局的接口调用类对象
        self.api_price_just = ApiPriceJust()
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

    def test_export_price_just_ok(self):
        """
        不输入任何条件，导出所有调价单
        """
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = ""
        pageSize = ""
        state = ""
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_ok pass")

    def test_export_brandName_ok(self):
        """
        输入品牌名称，导出调价单
        """
        brandName = "Chinstudio"
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = ""
        pageSize = ""
        state = ""
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_brandName_ok pass")

    def test_export_price_just_create_date_ok(self):
        """
        输入调价日期，导出调价单
        """
        brandName = ""
        createDateEnd = "2019-04-02"
        createDateStart = "2019-04-01"
        inventoryCode = ""
        pageNum = ""
        pageSize = ""
        state = ""
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_create_date_ok pass")

    def test_export_price_just_inventoryCode_ok(self):
        """
        输入调价日期，导出调价单
        """
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = "CH0001230BKS"
        pageNum = ""
        pageSize = ""
        state = ""
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_inventoryCode_ok pass")

    def test_export_price_just_pageNum_ok(self):
        """
        输入页码0，导出所有调价单
        """
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "0"
        pageSize = ""
        state = ""
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_pageNum_ok pass")

    def test_export_price_just_pageSize_ok(self):
        """
        输入每页条数0，导出所有调价单
        """
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = ""
        pageSize = "0"
        state = ""
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_pageSize_ok pass")

    def test_export_price_just_review_state_ok(self):
        """
        选择审核状态的调价单，导出调价单
        """
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = ""
        pageSize = ""
        state = "2"
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_review_state_ok pass")

    def test_export_price_just_open_state_ok(self):
        """
        选择开立状态的调价单，导出调价单
        """
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = ""
        pageSize = ""
        state = "0"
        vendorName = ""
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_open_state_ok pass")

    def test_export_price_just_vendorName_ok(self):
        """
        输入供应商名称，导出调价单
        """
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = ""
        pageSize = ""
        state = "0"
        vendorName = "测试CH0001230"
        # 2.调用接口
        body_data = ExportPrinceJust(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, inventoryCode=inventoryCode, pageNum=pageNum, pageSize=pageSize,
                                       state=state, vendorName=vendorName)
        response = self.api_price_just.get_price_just_export(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response(response, code, message, False)
        print("test_export_price_just_vendorName_ok pass")
