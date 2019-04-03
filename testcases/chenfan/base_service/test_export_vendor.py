__author__ = 'zzh'

import sys
import unittest  # 单元测试框架
from api_call.chenfan.base_service.api_vendor import ApiVendor
from data_structure.chenfan.base_service.data_vendor import ExportVendorAdd
from utils.restful import Restful

sys.path.insert(0, '..')


class TestExportVendor(unittest.TestCase):
    """
    供应商导出接口
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

    def test_export_vendor_ok(self):
        """
        不输入任何条件，导出所有供应商
        """
        category = ""
        coreproduct = ""
        factoryGrade = ""
        factorylocation = ""
        pageNum = ""
        pageSize = ""
        state = ""
        venAbbName = ""
        vendorCode = "00123"
        vensource = ""
        ventype = ""

        # 2.调用接口
        body_data = ExportVendorAdd(category=category, coreproduct=coreproduct, factoryGrade=factoryGrade, factorylocation=factorylocation, pageNum=pageNum, pageSize=pageSize,
                                       state=state, venAbbName=venAbbName, vendorCode=vendorCode, vensource=vensource, ventype=ventype)
        response = self.api_vendor.get_list_export(body_data)
        print(response)

