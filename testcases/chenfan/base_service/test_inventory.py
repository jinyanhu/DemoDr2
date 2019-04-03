
import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_inventory import ApiInventory
from data_structure.chenfan.base_service.data_inventory import *
from utils.restful import Restful
sys.path.insert(0, '..')


class TestInventory(unittest.TestCase):
    """
    存货档案相关接口
    """
    def setUp(self):

        self.api_inventory = ApiInventory()
        # 赋值self的其他字段
        self.restful = Restful()
        # 资源列表，用以回收资源
        self.service_id_list = list()

    def tearDown(self):
        pass

    def test_add_inventory(self):
        """
        正常新增存货档案列表
        :return:
        """
        body_data = [
                        {
                            "inventoryCode": "CH190401M",
                            "barcode": "CH190401M",
                            "color": "白色",
                            "size": "M",
                            "productCode": "CH190401",
                            "inventoryName": "CH190401",
                            "brandId": 2,
                            "newDate": "2019-04-30",
                            "inventoryCategory": "毛衣",
                            "invCCode": "110108",
                            "styleSource": "供款",
                            "season": "春",
                            "implementationStandards": "GB 5296.4-2012",
                            "level": "合格品",
                            "safetyTechnology": "GB 31701-A类",
                            "compositionName": "毛线",
                            "composition": "毛线",
                            "wmcategory": "类目四：羊毛衫、羊毛外套、粗纺外套",
                            "invCCode1": "11",
                            "brandName": "Chinstudio",
                            "createBy": "325",
                            "createDate": "2019-04-02",
                            "createName": "张晓方",
                            "inventoryClassId": 218,
                            "procodeCover": "",
                            "procodeImgs": ""
                        }
                    ]
        response = self.api_inventory.add_inventory(body_data=body_data)
        code = 200
        message = "新增存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResAddInventory(data_dec)
        print("test_add_inventory pass")

    def test_add_inventory_repeat(self):
        """
        重复新增存货档案
        :return:
        """
        body_data = [
                        {
                            "barcode": "CH181204L",
                            "brandId": "2",
                            "brandName": "Chinstudio",
                            "createPerson": "方丽颖",
                            "color": "白色",
                            "composition": "棉质",
                            "compositionName": "棉质",
                            "createBy": "176",
                            "createDate": "2018-08-01 00:00:00",
                            "createName": "方丽颖",
                            "finexcess": "0.1",
                            "img": "",
                            "implementationStandards": "",
                            "invCCode": "110101",
                            "inventoryCategory": "梭织",
                            "inventoryClassId": "215",
                            "inventoryCode": "CH181204L",
                            "inventoryName": "测试",
                            "level": "",
                            "newDate": "2018-08-27 00:00:00",
                            "premiumRate": "0.1",
                            "procodeCover": "",
                            "procodeImgs": "",
                            "productCode": "CH190401L",
                            "safetyTechnology": "",
                            "season": "夏",
                            "size": "L",
                            "styleSource": "自制",
                            "wmcategory": "类目二：棉袄"
                        }
                    ]
        response = self.api_inventory.add_inventory(body_data=body_data)
        code = 500
        message = "新增存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResAddInventory(data_dec)
        print("test_add_inventory_repeat pass")

    def test_add_inventory_no_productCode(self):
        """
        新增存货档案缺少货号
        :return:
        """
        body_data = [
                        {
                            "inventoryCode": "CH190401L",
                            "barcode": "CH190401L",
                            "color": "白色",
                            "size": "M",
                            "productCode": "",
                            "inventoryName": "接口测试",
                            "brandId": 2,
                            "newDate": "2019-04-30",
                            "inventoryCategory": "毛衣",
                            "invCCode": "110108",
                            "styleSource": "供款",
                            "season": "春",
                            "implementationStandards": "GB 5296.4-2012",
                            "level": "合格品",
                            "safetyTechnology": "GB 31701-A类",
                            "compositionName": "毛线",
                            "composition": "毛线",
                            "wmcategory": "类目四：羊毛衫、羊毛外套、粗纺外套",
                            "invCCode1": "11",
                            "brandName": "Chinstudio",
                            "createBy": "325",
                            "createDate": "2019-04-02",
                            "createName": "张晓方",
                            "inventoryClassId": 218,
                            "procodeCover": "",
                            "procodeImgs": ""
                        }
                    ]
        response = self.api_inventory.add_inventory(body_data=body_data)
        code = 500
        message = "新增存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResAddInventory(data_dec)
        print("test_add_inventory_repeat pass")

    def test_add_inventory_repeat_productCode(self):
        """
        新增存货档案货号重复
        :return:
        """
        body_data = [
                        {
                            "inventoryCode": "CH190402M",
                            "barcode": "CH190402M",
                            "color": "白色",
                            "size": "M",
                            "productCode": "CH181204",
                            "inventoryName": "CH190401",
                            "brandId": 2,
                            "newDate": "2019-04-30",
                            "inventoryCategory": "毛衣",
                            "invCCode": "110108",
                            "styleSource": "供款",
                            "season": "春",
                            "implementationStandards": "GB 5296.4-2012",
                            "level": "合格品",
                            "safetyTechnology": "GB 31701-A类",
                            "compositionName": "毛线",
                            "composition": "毛线",
                            "wmcategory": "类目四：羊毛衫、羊毛外套、粗纺外套",
                            "invCCode1": "11",
                            "brandName": "Chinstudio",
                            "createBy": "325",
                            "createDate": "2019-04-02",
                            "createName": "张晓方",
                            "inventoryClassId": 218,
                            "procodeCover": "",
                            "procodeImgs": ""
                        }
                    ]
        response = self.api_inventory.add_inventory(body_data=body_data)
        code = 500
        message = "新增存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResAddInventory(data_dec)
        print("test_add_inventory_repeat pass")

    def test_get_inventory_list(self):
        """
        查询所有存货档案列表
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode, isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list pass")

    def test_get_inventory_all_conditions(self):
        """
        所有条件都输入查询存货档案列表
        :return:
        """
        brandId = "2"
        invCName = "110119"
        inventoryCode = "CH61039WHM"
        isCraftsId = "1"
        newDateBegin = "2018-03-26 00:00:00"
        newDateEnd = "2018-03-26 23:00:00"
        productCode = "CH61039"
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode, isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_all_conditions pass")

    def test_get_inventory_list_brandId(self):
        """
        根据品牌id查询存货档案列表
        :return:
        """
        brandId = "2"
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode, isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_brandId pass")

    def test_get_inventory_list_productCode(self):
        """
        根据货号查询存货档案列表
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = "CH181204"
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode, isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_productCode pass")

    def test_get_inventory_list_inventoryCode(self):
        """
        根据存货编码查询存货档案列表
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = "CH181204S"
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode, isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_inventoryCode pass")

    def test_get_inventory_list_invCName(self):
        """
        根据存货分类查询存货档案列表
        :return:
        """
        brandId = ""
        invCName = "1101"
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                     isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_invCName pass")

    def test_get_inventory_list_newDate(self):
        """
        根据上新日期查询存货档案列表
        :return:
        """
        brandId = ""
        invCName = "1101"
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = "2019-02-27 00:00:00"
        newDateEnd = "2019-03-09 00:00:00"
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                     isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_newDate pass")

    def test_get_inventory_list_isCraftsId(self):
        """
        根据已有工艺单查询存货档案列表
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = "1"
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                     isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_isCraftsId pass")

    def test_get_inventory_list_no_isCraftsId(self):
        """
        根据没有工艺单查询存货档案列表
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = "0"
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                     isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_no_isCraftsId pass")

    def test_get_inventory_list_nothing(self):
        """
        查询不存在的存货档案
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = "CH99999"
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        pageSize = 30
        pageNum = 1
        total = 0
        body_data = GetInventoryList(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                     isCraftsId=isCraftsId,
                                     newDateBegin=newDateBegin, newDateEnd=newDateEnd, productCode=productCode,
                                     pageSize=pageSize, pageNum=pageNum, total=total)
        response = self.api_inventory.get_inventory_list(body_data=body_data)
        code = 200
        message = "查询存货档案列表失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryList(data_dec)
        print("test_get_inventory_list_no_isCraftsId pass")

    def test_get_inventory_info_productCode(self):
        """
        根据货号获取存货档案信息
        :return:
        """
        productCode = "CH181204"
        state = ""
        body_data = GetInventoryInfo(productCode=productCode, state=state)
        response = self.api_inventory.get_inventory_info(body_data=body_data)
        code = 200
        message = "获取存货档案信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryInfo(data_dec)
        print("test_get_inventory_info_productCode pass")

    def test_get_inventory_info_no_productCode(self):
        """
        不输入货号获取不到任何信息
        :return:
        """
        productCode = ""
        state = ""
        body_data = GetInventoryInfo(productCode=productCode, state=state)
        response = self.api_inventory.get_inventory_info(body_data=body_data)
        code = 200
        message = "获取存货档案信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryInfo(data_dec)
        print("test_get_inventory_info_no_productCode pass")

    def test_get_inventory_productCode_normal(self):
        """
        获取启用状态存货档案信息
        :return:
        """
        productCode = "CH181204"
        state = "0"
        body_data = GetInventoryInfo(productCode=productCode, state=state)
        response = self.api_inventory.get_inventory_info(body_data=body_data)
        code = 200
        message = "获取存货档案信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryInfo(data_dec)
        print("test_get_inventory_productCode_normal pass")

    def test_get_inventory_productCode_forbidden(self):
        """
        获取禁用状态存货档案信息
        :return:
        """
        productCode = "CH181204"
        state = "1"
        body_data = GetInventoryInfo(productCode=productCode, state=state)
        response = self.api_inventory.get_inventory_info(body_data=body_data)
        code = 200
        message = "获取存货档案信息失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResGetInventoryInfo(data_dec)
        print("test_get_inventory_productCode_forbidden pass")

    def test_export_inventory_all(self):
        """
        导出所有存货档案
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_all pass")

    def test_export_inventory_brandId(self):
        """
        按品牌导出存货档案
        :return:
        """
        brandId = "2"
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_brandId pass")

    def test_export_inventory_invCName(self):
        """
        按存货分类导出存货档案
        :return:
        """
        brandId = ""
        invCName = "1101"
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_invCName pass")

    def test_export_inventory_inventoryCode(self):
        """
        按存货编码导出存货档案
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = "ZZH666L"
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_inventoryCode pass")

    def test_export_inventory_productCode(self):
        """
        按货号导出存货档案
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = ""
        newDateEnd = ""
        productCode = "ZZH666"
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_productCode pass")

    def test_export_inventory_no_isCraftsId(self):
        """
        按没有工艺单导出存货档案
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = "0"
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_no_isCraftsId pass")

    def test_export_inventory_yes_isCraftsId(self):
        """
        按已有工艺单导出存货档案
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = "1"
        newDateBegin = ""
        newDateEnd = ""
        productCode = ""
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_yes_isCraftsId pass")

    def test_export_inventory_newDate(self):
        """
        按上新日期导出存货档案
        :return:
        """
        brandId = ""
        invCName = ""
        inventoryCode = ""
        isCraftsId = ""
        newDateBegin = "2018-02-27 00:00:00"
        newDateEnd = "2019-02-27 00:00:00"
        productCode = ""
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_newDate pass")

    def test_export_inventory_all_conditions(self):
        """
        输入所有条件导出存货档案
        :return:
        """
        brandId = "2"
        invCName = "1101"
        inventoryCode = "CH8412103BKS"
        isCraftsId = ""
        newDateBegin = "2018-02-27 00:00:00"
        newDateEnd = "2019-02-27 00:00:00"
        productCode = "CH8412103"
        body_data = ExportInventory(brandId=brandId, invCName=invCName, inventoryCode=inventoryCode,
                                    isCraftsId=isCraftsId, newDateBegin=newDateBegin, newDateEnd=newDateEnd,
                                    productCode=productCode)
        response = self.api_inventory.export_inventory(body_data=body_data)
        print("test_export_inventory_all_conditions pass")
    """
    def test_edit_inventory(self):
       
        barcode = "CH190403M"
        brandId = 2
        brandName = "Chinstudio"
        color = "黑色"
        composition = "12"
        compositionName = "12"
        createBy = "325"
        createDate = "2019-04-03"
        createName = "张晓方"
        implementationStandards = ""
        invCCode = "110101"
        invCCode1 = "11"
        invCName = "T恤"
        inventoryCategory = "牛仔"
        inventoryClassId = 215
        inventoryCode = "CH190403M"
        inventoryId = 61435
        inventoryName = "CH190403"
        level = ""
        newDate = "2019-04-29T16:00:00.000Z"
        procodeCover = ""
        procodeImgs = ""
        productCode = "CH190403"
        safetyTechnology = ""
        season = "春"
        size = "M"
        state = 0
        styleSource = "供款"
        wmcategory = "类目一：单裙、连衣裙、裤子外套、牛仔"
        body_data = EditInventory(barcode=barcode, brandId=brandId, brandName=brandName, color=color, composition=composition, compositionName=compositionName,
                                  createBy=createBy, createDate=createDate, createName=createName, implementationStandards=implementationStandards, invCCode=invCCode,
                                  invCCode1=invCCode1, invCName=invCName, inventoryCategory=inventoryCategory, inventoryClassId=inventoryClassId, inventoryCode=inventoryCode,
                                  inventoryId=inventoryId, inventoryName=inventoryName, level=level, newDate=newDate, procodeCover=procodeCover, procodeImgs=procodeImgs,
                                  productCode=productCode, safetyTechnology=safetyTechnology, season=season, size=size,
                                  state=state, styleSource=styleSource, wmcategory=wmcategory)
        response = self.api_inventory.edit_inventory(body_data=body_data)
        code = 200
        message = "修改存货档案失败"
        data_dec = self.restful.parse_response_text(response, code, message)
        ResEditInventory(data_dec)
        print("test_edit_inventory pass")
        """
