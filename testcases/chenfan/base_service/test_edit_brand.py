
import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_brand import ApiBrand
from data_structure.chenfan.base_service.data_brand import DataEditBrand
from data_structure.chenfan.base_service.data_brand import DataResEditBrand
from utils.restful import Restful
sys.path.insert(0, '..')


class TeatEdieBrand(unittest.TestCase):
    """
    品牌修改接口
    """
    def setUp(self):
        self.api_brand = ApiBrand()
        # 赋值self的其他字段
        self.restful = Restful()
        # 资源列表，用以回收资源
        self.service_id_list = list()

    def tearDown(self):
        pass

    def test_edit_brand(self):
        """
        正常修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00012"
        brandName = "接口自动化品牌1"
        brandType = "1"
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
        updateBy = "325"
        updateName = "张晓方"
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 200
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand pass")

    def test_edit_brand_no_brandName(self):
        """
        不输入品牌名称修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00019"
        brandName = ""
        brandType = "1"
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
        updateBy = "325"
        updateName = "张晓方"
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.create_brand(body_data=body_data)
        code = 400
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_brandName pass")

    def test_edit_brand_no_customerId(self):
        """
        不输入客户ID修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00019"
        brandName = "接口自动化品牌"
        brandType = "1"
        customerId = ""
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
        updateBy = "325"
        updateName = ""
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_customerId pass")

    def test_edit_brand_no_customerName(self):
        """
        不输入客户名称修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "0012"
        brandName = "接口自动化品牌"
        brandType = "1"
        customerId = 19
        customerName = ""
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
        updateBy = "325"
        updateName = "张晓方"
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_customerName pass")

    def test_edit_brand_no_magnification(self):
        """
        不输入倍率修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00019"
        brandName = "接口自动化品牌1"
        brandType = 1
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
        updateBy = "325"
        updateName = ""

        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_magnification pass")

    def test_edit_brand_no_lowestVendorLevel(self):
        """
        不输入供应商最低等级修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "0012"
        brandName = "接口自动化品牌1"
        brandType = "1"
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
        updateBy = "325"
        updateName = ""

        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_lowestVendorLevel pass")

    def test_edit_brand_no_receiveAddress(self):
        """
        不输入收货地址修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00019"
        brandName = "接口自动化品牌1"
        brandType = "1"
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
        receiveAddress = ""
        receiveName = "收货人"
        receiveTel = "11122334"
        state = 1
        updateBy = "325"
        updateName = "张晓方"
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_receiveAddress pass")

    def test_edit_brand_no_receiveName(self):
        """
        不输入收货人修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00019"
        brandName = "接口自动化品牌1"
        brandType = "1"
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
        receiveName = ""
        receiveTel = "11122334"
        state = 1
        updateBy = "325"
        updateName = "张晓方"
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_receiveName pass")

    def test_edit_brand_no_receiveTel(self):
        """
        不输入联系电话修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00019"
        brandName = "接口自动化品牌1"
        brandType = "1"
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
        receiveTel = ""
        state = 1
        updateBy = "325"
        updateName = "张晓方"
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_receiveName pass")

    def test_edit_brand_no_prefixEn(self):
        """
        不输入前缀修改品牌
        :return:
        """
        # 准备参数
        brandId = "32"
        brandCode = "00019"
        brandName = "接口自动化品牌1"
        brandType = "1"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11.00
        lowestPerformanceScore = 22.00
        lowestPostSaleDefectiveScore = 33.00
        lowestPreSaleDefectiveScore = 22.00
        lowestReOrderPeriodScore = 22.00
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = ""
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "1254656"
        state = 1
        updateBy = "325"
        updateName = "张晓方"
        # 调用数据处理类，将参数合并到字典中
        body_data = DataEditBrand(brandCode=brandCode, brandName=brandName, brandType=brandType,
                                  customerId=customerId, customerName=customerName,
                                  magnification=magnification, prefixEn=prefixEn, receiveAddress=receiveAddress,
                                  receiveName=receiveName, receiveTel=receiveTel, state=state,
                                  lowestOnTimeReachScore=lowestOnTimeReachScore,
                                  lowestPerformanceScore=lowestPerformanceScore,
                                  lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                  lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                  lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                  lowestVendorLevel=lowestVendorLevel, updateBy=updateBy, updateName=updateName,
                                  brandId=brandId)
        # 调用品牌创建接口
        response = self.api_brand.edit_brand(body_data=body_data)
        code = 400
        message = "修改品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResEditBrand(data_dec)
        print("test_edit_brand_no_prefixEn pass")
