__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_priceJust import ApiPriceJust
from data_structure.chenfan.base_service.data_priceJust import DataPriceJustUpdateState
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustUpdateState
from utils.restful import Restful

sys.path.insert(0, '..')


class TestPriceJustUpdate(unittest.TestCase):
    """
     存货调价单审核接口
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

    def test_update_priceJust_state_ok(self):
        """
        正常审核存货调价单
        """
        # 1.输入必填的参数
        priceJustCodes = "QTJ201904080010"
        # 2.调用接口
        body_data = DataPriceJustUpdateState(priceJustCodes=priceJustCodes)
        response = self.api_price_just.put_update(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdateState(data_dec)
        # 更新调价单的状态，已审核修改为已确认状态
        sql = "update price_just_main set state=1 where price_just_code = '{}'".format(priceJustCodes)
        self.api_price_just.update_price_just(sql)
        print("test_update_priceJust_state_ok pass")

    def test_update_Checked_priceJust_state_fail(self):
        """
        审核“已审核状态”的调价单，无法审核成功
        """
        # 1.输入必填的参数
        priceJustCodes = "QTJ201903260009"
        # 2.调用接口
        body_data = DataPriceJustUpdateState(priceJustCodes=priceJustCodes)
        response = self.api_price_just.put_update(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "调价单已经审核"
        code = 500
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdateState(data_dec)
        # 更新调价单的状态，已审核修改为已确认状态
        print("test_update_Checked_priceJust_state_fail pass")

    def test_update_error_priceJust_code_state_fail(self):
        """
        审核“已审核状态”的调价单，无法审核成功
        """
        # 1.输入必填的参数
        priceJustCodes = "123456"
        # 2.调用接口
        body_data = DataPriceJustUpdateState(priceJustCodes=priceJustCodes)
        response = self.api_price_just.put_update(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "调价单号错误，审核失败"
        code = 500
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdateState(data_dec)
        # 更新调价单的状态，已审核修改为已确认状态
        print("test_update_error_priceJust_code_state_fail pass")