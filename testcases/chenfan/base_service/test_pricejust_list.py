__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_priceJust import ApiPriceJust
from data_structure.chenfan.base_service.data_priceJust import DataPriceJustList
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustList
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustListError
from utils.restful import Restful

sys.path.insert(0, '..')


class TestPriceJustList(unittest.TestCase):
    """
    获取存货调价单列表接口
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

    def test_look_all_priceJust_list_ok(self):
        """
        列表不输入查询条件，查看全部存货调价单
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = ""
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_look_all_priceJust_list_ok pass")

    def test_input_priceJustCode_look_priceJust_list_ok(self):
        """
        列表输入调价单号，查看对应的存货调价单
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = "QTJ201904090001"
        state = ""
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_input_priceJustCode_look_priceJust_list_ok pass")

    def test_input_error_priceJustCode_look_priceJust_list_fail(self):
        """
        列表输入不存在的调价单号，查看存货调价单失败
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = "123123"
        state = ""
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustListError(data_dec)
        print("test_input_error_priceJustCode_look_priceJust_list_fail pass")

    def test_input_review_state_look_priceJust_list_ok(self):
        """
        单据状态选择已审核，查看对应的存货调价单
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = "2"
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_input_review_state_look_priceJust_list_ok pass")

    def test_input_open_state_look_priceJust_list_ok(self):
        """
        单据状态选择开立，查看对应的存货调价单
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = "1"
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_input_open_state_look_priceJust_list_ok pass")

    def test_input_inventoryCode_look_priceJust_list_ok(self):
        """
        输入存货编码，查看对应的存货调价单
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = "CS001BK35"
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = ""
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_input_inventoryCode_look_priceJust_list_ok pass")

    def test_input_error_inventoryCode_look_priceJust_list_fail(self):
        """
        输入不存在的存货编码，查看存货调价单失败
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = "123123213"
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = ""
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustListError(data_dec)
        print("test_input_error_inventoryCode_look_priceJust_list_fail pass")

    def test_input_brandName_look_priceJust_list_ok(self):
        """
        输入品牌名称，查看对应的存货调价单
        """
        # 1.输入必填的参数
        brandName = "2"
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = ""
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_input_brandName_look_priceJust_list_ok pass")

    def test_input_createDateStart_createDateEnd_look_priceJust_list_ok(self):
        """
        输入调价开始和结束日期，查看对应的存货调价单
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = "2019-04-09 23:59:59"
        createDateStart = "2019-04-01 00:00:00"
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = ""
        vendorId= ""
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_input_createDateStart_createDateEnd_look_priceJust_list_ok pass")

    def test_input_vendorId_look_priceJust_list_ok(self):
        """
        输入供应商，查看对应的存货调价单
        """
        # 1.输入必填的参数
        brandName = ""
        createDateEnd = ""
        createDateStart = ""
        inventoryCode = ""
        pageNum = "1"
        pageSize = "30"
        priceJustCode = ""
        state = ""
        vendorId= "28"
        vendorName = ""
        # 2.调用接口
        body_data = DataPriceJustList(brandName=brandName, createDateEnd=createDateEnd, createDateStart=createDateStart, pageNum=pageNum, pageSize=pageSize, inventoryCode=inventoryCode, priceJustCode=priceJustCode, state=state, vendorId=vendorId, vendorName=vendorName)
        response = self.api_price_just.get_price_just_list(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustList(data_dec)
        print("test_input_vendorId_look_priceJust_list_ok pass")

