__author__ = 'zzh'

import sys
import unittest  # 单元测试框架
import json

from api_call.chenfan.base_service.api_priceJust import ApiPriceJust
from data_structure.chenfan.base_service.data_priceJust import DataPriceJustUpdate
from data_structure.chenfan.base_service.data_priceJust import DataResPriceJustUpdate
from utils.restful import Restful

sys.path.insert(0, '..')


class TestUpdatePriceJust(unittest.TestCase):
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

    def test_update_factoryQuote_priceJust_ok(self):
        """
        修改工厂报价，可以修改成功
        """
        body_data = [
            {
                "brandId": "2",
                "brandName": "Chinstudio",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "100000",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "13",
                "taxUnitPrice": 100,
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢植敏",
                "vendorCode": "00229",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_factoryQuote_priceJust_ok pass")

    def test_update_null_factoryQuote_priceJust_fail(self):
        """
        不输入工厂报价，修改调价单失败
        """
        body_data = [
            {
                "brandId": "2",
                "brandName": "Chinstudio",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "100000",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "13",
                "taxUnitPrice": 100,
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢植敏",
                "vendorCode": "00229",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_null_factoryQuote_priceJust_fail pass")

    def test_update_remark_priceJust_ok(self):
        """
        修改调价原因，可以修改成功
        """
        body_data = [
            {
                "brandId": "2",
                "brandName": "Chinstudio",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "123456测试",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "13",
                "taxUnitPrice": 100,
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢植敏",
                "vendorCode": "00229",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_remark_priceJust_ok pass")

    def test_update_taxUnitPrice_priceJust_ok(self):
        """
        修改含税单价，可以修改成功
        """
        body_data = [
            {
                "brandId": "2",
                "brandName": "Chinstudio",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "123456测试",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "13",
                "taxUnitPrice": 200,
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢植敏",
                "vendorCode": "00229",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_taxUnitPrice_priceJust_ok pass")

    def test_update_null_taxUnitPrice_priceJust_fail(self):
        """
        不输入含税单价，修改失败
        """
        body_data = [
            {
                "brandId": "2",
                "brandName": "Chinstudio",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "123456测试",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "13",
                "taxUnitPrice": "",
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢植敏",
                "vendorCode": "00229",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_null_taxUnitPrice_priceJust_fail pass")

    def test_update_taxRate_priceJust_ok(self):
        """
        修改税率，可以修改成功
        """
        body_data = [
            {
                "brandId": "2",
                "brandName": "Chinstudio",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "123456测试",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "16",
                "taxUnitPrice": 200,
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢植敏",
                "vendorCode": "00229",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_taxRate_priceJust_ok pass")

    def test_update_venAbbName_priceJust_ok(self):
        """
        修改供应商，可以修改成功
        """
        body_data = [
            {
                "brandId": "2",
                "brandName": "Chinstudio",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "123456测试",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "16",
                "taxUnitPrice": 200,
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢亮",
                "vendorCode": "00228",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_venAbbName_priceJust_ok pass")

    def test_update_brandName_priceJust_ok(self):
        """
        修改品牌，可以修改成功
        """
        body_data = [
            {
                "brandId": "4",
                "brandName": "草莓跳 小跳家",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "123456测试",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "16",
                "taxUnitPrice": 200,
                "unitPrice": 88.4956,
                "updateName": "金严虎测试",
                "venAbbName": "谢亮",
                "vendorCode": "00228",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_brandName_priceJust_ok pass")

    def test_update_unitPrice_priceJust_ok(self):
        """
        修改不含税单价，可以修改成功
        """
        body_data = [
            {
                "brandId": "4",
                "brandName": "草莓跳 小跳家",
                "color": "黑",
                "createDate": "2019-04-08 17:27:07",
                "createName": "张志河",
                "factoryQuote": "500",
                "flag": 1,
                "inventoryCode": "CH0001230BKS",
                "inventoryCover": "",
                "inventoryId": "61308",
                "inventoryName": "测试CH0001230",
                "priceJustCode": "QTJ201904080019",
                "priceJustDetailId": 1100058236,
                "productCode": "CH0001230",
                "remark": "123456测试",
                "season": "夏",
                "size": "S",
                "state": 0,
                "taxRate": "16",
                "taxUnitPrice": 200,
                "unitPrice": 188,
                "updateName": "金严虎测试",
                "venAbbName": "谢亮",
                "vendorCode": "00228",
                "vendorId": 63,
                "verifier": "张志河",
                "verifydate": "2019-04-08 18:21:41"

            }
        ]

        response = self.api_price_just.put_update_price_just(body_data)

        # 3.获取响应数据，判断状态码，并获取“data”
        message = "success"
        code = 200
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, message)

        # 4.设置数据并在内部验证完整性
        DataResPriceJustUpdate(data_dec)
        print("test_update_unitPrice_priceJust_ok pass")



