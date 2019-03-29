
import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_brand import ApiBrand
from data_structure.chenfan.base_service.data_brand import DataResCreateBrand
from data_structure.chenfan.base_service.data_brand import DataCreateBrand
from utils.restful import Restful
sys.path.insert(0, '..')


class TeatCreateBrand(unittest.TestCase):
    """
    品牌创建接口
    """
    def setUp(self):
        self.api_brand = ApiBrand()
        # 赋值self的其他字段
        self.restful = Restful()
        # 资源列表，用以回收资源
        self.service_id_list = list()

    def tearDown(self):
        pass

    def test_create_brand(self):
        """
        正常创建品牌
        :return:
        """
        # 准备参数
        brandCode = "00012"
        brandName = "接口自动化品牌2"
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = "JHL"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1
        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 200
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        sql = "DELETE FROM brand WHERE brand_code = '00012'"
        self.api_brand.delete_brand(sql=sql)
        print("test_create_brand pass")

    """
    def test_create_brand_no_brandCode(self):
        
        # 准备参数
        brandCode = ""
        brandName = "接口自动化品牌"
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = "JKL"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1
        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 400
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand_no_brandCode pass")
    """
    def test_create_brand_no_brandName(self):
        """
        不输入品牌名称创建品牌
        :return:
        """
        # 准备参数
        brandCode = "0012"
        brandName = ""
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = "JL"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1
        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 400
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand_no_brandName pass")

    """"
    def test_create_brand_no_customerId(self):
        
        # 准备参数
        brandCode = "0012"
        brandName = "接口自动化品牌2"
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = ""
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = "JSL"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1
        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 401
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand_no_customerId pass")
    """
    """
    def test_create_brand_no_customerName(self):
        
        # 准备参数
        brandCode = "0012"
        brandName = "接口自动化品牌"
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = 19
        customerName = ""
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = "JDL"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1

        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 400
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand_no_customerName pass")
    """

    def test_create_brand_no_magnification(self):
        """
        不输入倍率创建品牌
        :return:
        """
        # 准备参数
        brandCode = "0012"
        brandName = "接口自动化品牌3"
        brandType = 1
        createBy = 325
        createName = "张晓方"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = ""
        prefixEn = "JLJ"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1

        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 400
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand_no_magnification pass")

    def test_create_brand_no_lowestVendorLevel(self):
        """
        不输入供应商最低等级创建品牌
        :return:
        """
        # 准备参数
        brandCode = "0012"
        brandName = "接口自动化品牌1"
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = ""
        magnification = "1.1"
        prefixEn = "HJK"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1

        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 400
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand_no_lowestVendorLevel pass")

    """
    def test_create_brand_no_receiveAddress(self):
        
        # 准备参数
        brandCode = "00012"
        brandName = "接口自动化品牌4"
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = "JFL"
        receiveAddress = ""
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1

        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 400
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand_no_lowestVendorLevel pass")
    """
