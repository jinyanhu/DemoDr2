
import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_inventory import ApiInventory
from data_structure.chenfan.base_service.data_inventory import *
from utils.restful import Restful
sys.path.insert(0, '..')


class TeatPublic(unittest.TestCase):
    """
    品牌创建接口
    """
    def setUp(self):
        self.api_inventory = ApiInventory()
        # 赋值self的其他字段
        self.restful = Restful()
        # 资源列表，用以回收资源
        self.service_id_list = list()

    def tearDown(self):
        pass

    def test_get_brand_info_list(self):
        """
        获取全部品牌信息
        :return:
        """
        brandid = ""
        brandname = ""
        state = ""
        body_data = GetBrandList(brandid=brandid, brandname=brandname, state=state)
        response = self.api_inventory.get_brand_list(body_data=body_data)
        code = 200
        message = "获取品牌信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        # 断言接口返回的数据
        ResGetBrandList(data_dec)
        print("test_get_brand_info_list pass")

    def test_get_inventory_class_list(self):
        """
        获取全部存货分类
        :return:
        """
        invCCode = None
        invCCode1 = None
        invCCode3 = None
        invCEnd = None
        invCGrade = None
        invCName = None
        inventoryClassId = None
        body_data = GetInventoryClassInfoList(invCCode=invCCode, invCCode1=invCCode1, invCCode3=invCCode3, invCEnd=invCEnd,
                                              invCGrade=invCGrade, invCName=invCName, inventoryClassId=inventoryClassId)
        response = self.api_inventory.get_inventory_class_info_list(body_data=body_data)
        code = 200
        message = "获取品牌信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryClassInfoList(data_dec)
        print("test_get_inventory_class_list pass")

    def test_get_inventory_class_list_invCGrade1(self):
        """
        获取一级类目
        :return:
        """
        invCCode = 11
        invCCode1 = None
        invCCode3 = None
        invCEnd = None
        invCGrade = 1
        invCName = None
        inventoryClassId = None
        body_data = GetInventoryClassInfoList(invCCode=invCCode, invCCode1=invCCode1, invCCode3=invCCode3, invCEnd=invCEnd,
                                              invCGrade=invCGrade, invCName=invCName, inventoryClassId=inventoryClassId)
        response = self.api_inventory.get_inventory_class_info_list(body_data=body_data)
        code = 200
        message = "获取品牌信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryClassInfoList(data_dec)
        print("test_get_inventory_class_list pass")

    def test_get_inventory_class_list_invCGrade2(self):
        """
        获取二级类目
        :return:
        """
        invCCode = 1101
        invCCode1 = None
        invCCode3 = None
        invCEnd = None
        invCGrade = 2
        invCName = None
        inventoryClassId = None
        body_data = GetInventoryClassInfoList(invCCode=invCCode, invCCode1=invCCode1, invCCode3=invCCode3, invCEnd=invCEnd,
                                              invCGrade=invCGrade, invCName=invCName, inventoryClassId=inventoryClassId)
        response = self.api_inventory.get_inventory_class_info_list(body_data=body_data)
        code = 200
        message = "获取品牌信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryClassInfoList(data_dec)
        print("test_get_inventory_class_list pass")

    def test_get_inventory_class_list_invCGrade3(self):
        """
        获取三级级类目
        :return:
        """
        invCCode = 110101
        invCCode1 = None
        invCCode3 = None
        invCEnd = None
        invCGrade = 3
        invCName = None
        inventoryClassId = None
        body_data = GetInventoryClassInfoList(invCCode=invCCode, invCCode1=invCCode1, invCCode3=invCCode3, invCEnd=invCEnd,
                                              invCGrade=invCGrade, invCName=invCName, inventoryClassId=inventoryClassId)
        response = self.api_inventory.get_inventory_class_info_list(body_data=body_data)
        code = 200
        message = "获取品牌信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryClassInfoList(data_dec)
        print("test_get_inventory_class_list pass")

    def test_get_size_sort_info_list(self):
        """
        获取尺码排序表信息
        :return:
        """
        response = self.api_inventory.get_size_sort_info_list()
        code = 200
        message = "获取品牌信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetSizeSortInfoList(data_dec)
        print("test_get_size_sort_info_list pass")
