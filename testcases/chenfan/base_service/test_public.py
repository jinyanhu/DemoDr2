
import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_inventory import ApiInventory
from data_structure.chenfan.base_service.data_inventory import *
from utils.restful import Restful
sys.path.insert(0, '..')


class TeatPublic(unittest.TestCase):
    """
    公共接口
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

    def test_get_style_info(self):
        """
        获取尺码排序表信息
        :return:
        """
        response = self.api_inventory.get_style_info()
        code = 200
        message = "获取品牌信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetStyleInfo(data_dec)
        print("test_get_style_info pass")

    def test_export_inventory_qualified_all(self):
        """
        按合格证模板导出所有
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_all pass")

    def test_export_inventory_qualified_brandId(self):
        """
        合格证模板按品牌导出
        :return:
        """
        brandId = "2"
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_brandId pass")

    def test_export_inventory_qualified_invCName(self):
        """
        合格证模板按存货分类导出
        :return:
        """
        brandId = ""
        invCName = "1101"
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_invCName pass")

    def test_export_inventory_qualified_inventoryCode(self):
        """
        合格证模板按存货编码导出
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = "ZZH666L"
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_inventoryCode pass")

    def test_export_inventory_qualified_productCode(self):
        """
        合格证模板按货号导出
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = "ZZH666"
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_productCode pass")

    def test_export_inventory_qualified_no_isCraftsId(self):
        """
        合格证模板按没有工艺单导出
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = "0"
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_no_isCraftsId pass")

    def test_export_inventory_qualified_yes_isCraftsId(self):
        """
        合格证模板按已有工艺单导出
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = "1"
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_yes_isCraftsId pass")

    def test_export_inventory_qualified_newDate(self):
        """
        合格证模板按上新日期导出
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = "2018-02-27 00:00:00"
        newDateEnd = "2019-02-27 00:00:00"
        productCode = ""
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_newDate pass")

    def test_export_inventory_qualified_all_conditions(self):
        """
        合格证模板输入所有条件导出
        :return:
        """
        brandId = "2"
        invCName = "1101"
        inventoryCode = "CH8412103BKS"
        isCraftsId = ""
        newDateBegin = "2018-02-27 00:00:00"
        newDateEnd = "2019-02-27 00:00:00"
        productCode = "CH8412103"
        body_data = ExportInventoryQualified(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                             isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                             productCode=productCode)
        response = self.api_inventory.export_inventory_qualified(body_data=body_data)
        print("test_export_inventory_qualified_newDate pass")

    def test_switch_state_one_forbidden(self):
        """
        禁用一个存货档案
        :return:
        """
        inventoryIds = [61430]
        state = "1"
        body_data = SwitchState(inventoryIds=inventoryIds, state=state)
        response = self.api_inventory.switch_state(body_data=body_data)
        code = 200
        message = "禁用存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResSwitchState(data_dec)
        print("test_switch_state_one_forbidden pass")

    def test_switch_state_one_startUse(self):
        """
        启用一个存货档案
        :return:
        """
        inventoryIds = [61430]
        state = "0"
        body_data = SwitchState(inventoryIds=inventoryIds, state=state)
        response = self.api_inventory.switch_state(body_data=body_data)
        code = 200
        message = "启用存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResSwitchState(data_dec)
        print("test_switch_state_one_forbidden pass")

    def test_switch_state_more_forbidden(self):
        """
        禁用多个存货档案
        :return:
        """
        inventoryIds = [61430, 61431, 61432, 61433]
        state = "1"
        body_data = SwitchState(inventoryIds=inventoryIds, state=state)
        response = self.api_inventory.switch_state(body_data=body_data)
        code = 200
        message = "禁用存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResSwitchState(data_dec)
        print("test_switch_state_one_forbidden pass")

    def test_switch_state_more_startUse(self):
        """
        启用多个存货档案
        :return:
        """
        inventoryIds = [61430, 61431, 61432, 61433]
        state = "0"
        body_data = SwitchState(inventoryIds=inventoryIds, state=state)
        response = self.api_inventory.switch_state(body_data=body_data)
        code = 200
        message = "启用存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResSwitchState(data_dec)
        print("test_switch_state_one_forbidden pass")

    def test_switch_state_startUse_nothing(self):
        """
        启用不存在的存货档案
        :return:
        """
        inventoryIds = [61420]
        state = "0"
        body_data = SwitchState(inventoryIds=inventoryIds, state=state)
        response = self.api_inventory.switch_state(body_data=body_data)
        code = 500
        message = "启用存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResSwitchState(data_dec)
        print("test_switch_state_startUse_nothing pass")

    def test_switch_state_forbidden_nothing(self):
        """
        禁用不存在的存货档案
        :return:
        """
        inventoryIds = [61420]
        state = "1"
        body_data = SwitchState(inventoryIds=inventoryIds, state=state)
        response = self.api_inventory.switch_state(body_data=body_data)
        code = 500
        message = "启用存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResSwitchState(data_dec)
        print("test_switch_state_forbidden_nothing pass")
