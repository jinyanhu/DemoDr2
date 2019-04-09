__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_priceJust import ApiPriceJust
from data_structure.chenfan.base_service.data_priceJust import DataPriceJustDetail
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustDetail
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustDetail1
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustDetail2
from utils.restful import Restful

sys.path.insert(0, '..')


class TestPriceJustDetail(unittest.TestCase):
    """
    查看存货调价单详情接口
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

    def test_view_priceJust_detail_ok(self):
        """
        正常查看存货调价单详情
        """
        # 1.输入必填的参数
        priceJustCode = "QTJ201904080010"
        # 2.调用接口
        body_data = DataPriceJustDetail(priceJustCode)
        response = self.api_price_just.get_detail(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustDetail(data_dec)
        print("test_view_priceJust_detail_ok pass")

    def test_view_null_priceJust_detail_fail(self):
        """
        不输入存货调价单，查看存货调价单详情失败
        """
        # 1.输入必填的参数
        priceJustCode = ""
        # 2.调用接口
        body_data = DataPriceJustDetail(priceJustCode=priceJustCode)
        response = self.api_price_just.get_detail(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "调价单号不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustDetail2(data_dec)
        print("test_view_null_priceJust_detail_fail pass")

    def test_view_error_priceJust_detail_fail(self):
        """
        输入不存在的调价单号，查询的结果为空
        """
        # 1.输入必填的参数
        priceJustCode = "1231233"
        # 2.调用接口
        body_data = DataPriceJustDetail(priceJustCode=priceJustCode)
        response = self.api_price_just.get_detail(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)
        # 4.设置数据并在内部验证完整性
        DataResPriceJustDetail1(data_dec)
        print("test_view_error_priceJust_detail_fail pass")

