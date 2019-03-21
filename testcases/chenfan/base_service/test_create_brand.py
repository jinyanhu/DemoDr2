
import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_brand import ApiBrand,ApiCreateBrand
from data_structure.chenfan.base_service.data_brand import DataBrand
from data_structure.chenfan.base_service.data_brand import DataResBrand
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
        self.api_create_brand = ApiCreateBrand()
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
        brandCode = "00011"
        brandName = "接口自动化品牌"
        brandType = "1"
        createBy = "325"
        createName = "张晓方"
        customerId = 19
        customerName = "杭州宸帆电子商务有限责任公司"
        lowestOnTimeReachScore = 11
        lowestPerformanceScore = 22
        lowestPostSaleDefectiveScore = 33
        lowestPreSaleDefectiveScore = 22
        lowestReOrderPeriodScore = 33
        lowestVendorLevel = "A"
        magnification = "1.1"
        prefixEn = "JK"
        receiveAddress = "地址"
        receiveName = "收货人"
        receiveTel = "11122334455"
        state = 1

        # 调用数据处理类，将参数合并到字典中
        body_data = DataCreateBrand(brandCode=brandCode, brandName=brandName, brandType=brandType, createBy=createBy,
                                    createName=createName, customerId=customerId, customerName=customerName,
                                    magnification=magnification,prefixEn=prefixEn, receiveAddress=receiveAddress,
                                    receiveName=receiveName, receiveTel=receiveTel, state=state,
                                    lowestOnTimeReachScore=lowestOnTimeReachScore,
                                    lowestPerformanceScore=lowestPerformanceScore,
                                    lowestPostSaleDefectiveScore=lowestPostSaleDefectiveScore,
                                    lowestPreSaleDefectiveScore=lowestPreSaleDefectiveScore,
                                    lowestReOrderPeriodScore=lowestReOrderPeriodScore,
                                    lowestVendorLevel=lowestVendorLevel)
        # 调用品牌创建接口
        response = self.api_create_brand.create_brand(body_data=body_data)
        code = 200
        message = "创建品牌失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        DataResCreateBrand(data_dec)
        print("test_create_brand pass")
