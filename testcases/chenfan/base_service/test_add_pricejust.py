__author__ = 'zzh'

import sys
import unittest  # 单元测试框架

from api_call.chenfan.base_service.api_priceJust import ApiPriceJust
from data_structure.chenfan.base_service.data_priceJust import DataPriceJustAdd
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustAdd
from utils.restful import Restful

sys.path.insert(0, '..')


class TestAddPriceJust(unittest.TestCase):
    """
    存货调价单新增接口
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

    def test_add_priceJust_ok(self):
        """
        正常新增存货调价单
        """
        gain_price_code = self.api_price_just.get_price_just_code()
        body_data = {
                            "detailReqModels": [
                                                 {
                                                    "brandId": 2,
                                                    "brandName": "Chinstudio",
                                                    "color": "黑",
                                                    "factoryQuote": "100",
                                                    "inventoryCode": "CH0001230BKS",
                                                    "inventoryId": "61308",
                                                    "inventoryName": "测试CH0001230",
                                                    "newDate": "2019-03-26",
                                                    "productCode": "CH0001230",
                                                    "remark": "100000",
                                                    "season": "夏",
                                                    "size": "S",
                                                    "taxRate": "13",
                                                    "taxUnitPrice": "100",
                                                    "unitPrice": "88.4956",
                                                    "vendorCode": "00229",
                                                    "vendorId": "63"
                                                 }
                                            ],
                            "mainReqModel": {
                                                    "ddate": "2019-04-04",
                                                    "maker": "金严虎测试",
                                                    "priceJustCode": "{}".format(gain_price_code)
                                            }

                        }

        # 2.调用接口
        response = self.api_price_just.post_add_price(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustAdd(data_dec)
        print("test_add_priceJust_ok pass")

    def test_null_factoryQuote_add_price_just_fail(self):
        """
        不输入工厂报价，创建存货调价单失败
        """
        gain_price_code = self.api_price_just.get_price_just_code()
        body_data = {
                            "detailReqModels": [
                                                 {
                                                    "brandId": 2,
                                                    "brandName": "chinstudio",
                                                    "color": "黑",
                                                    "factoryQuote": "",
                                                    "inventoryCode": "CH0001230BKS",
                                                    "inventoryId": "61308",
                                                    "inventoryName": "测试CH0001230",
                                                    "newDate": "2019-03-26",
                                                    "productCode": "CH0001230",
                                                    "remark": "100000",
                                                    "season": "夏",
                                                    "size": "S",
                                                    "taxRate": "13",
                                                    "taxUnitPrice": "100",
                                                    "unitPrice": "88.4956",
                                                    "vendorCode": "00229",
                                                    "vendorId": "63"
                                                 }
                                            ],
                            "mainReqModel": {
                                                    "ddate": "2019-04-04",
                                                    "maker": "金严虎测试",
                                                    "priceJustCode": "{}".format(gain_price_code)
                                            }

                        }

        # 2.调用接口
        response = self.api_price_just.post_add_price(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "工厂报价不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustAdd(data_dec)
        print("test_null_factoryQuote_add_price_just_fail pass")

    def test_null_inventoryCode_add_price_just_fail(self):
        """
        不输入存货编码，创建存货调价单失败
        """
        gain_price_code = self.api_price_just.get_price_just_code()
        body_data = {
                            "detailReqModels": [
                                                 {
                                                    "brandId": 2,
                                                    "brandName": "chinstudio",
                                                    "color": "黑",
                                                    "factoryQuote": "100",
                                                    "inventoryCode": "",
                                                    "inventoryId": "61308",
                                                    "inventoryName": "测试CH0001230",
                                                    "newDate": "2019-03-26",
                                                    "productCode": "CH0001230",
                                                    "remark": "100000",
                                                    "season": "夏",
                                                    "size": "S",
                                                    "taxRate": "13",
                                                    "taxUnitPrice": "100",
                                                    "unitPrice": "88.4956",
                                                    "vendorCode": "00229",
                                                    "vendorId": "63"
                                                 }
                                            ],
                            "mainReqModel": {
                                                    "ddate": "2019-04-04",
                                                    "maker": "金严虎测试",
                                                    "priceJustCode": "{}".format(gain_price_code)
                                            }

                        }

        # 2.调用接口
        response = self.api_price_just.post_add_price(body_data=body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "存货编码不能为空"
        code = 400
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustAdd(data_dec)
        print("test_null_inventoryCode_add_price_just_fail pass")


