

import sys
import unittest  # 单元测试框架
import time

from api_call.chenfan.base_service.api_route import ApiRoute
from data_structure.chenfan.base_service.data_esb import DataRouteEsb
from data_structure.chenfan.base_service.data_esb import DataResEsb
from utils.restful import Restful

sys.path.insert(0, '..')


class TestEsbReturn(unittest.TestCase):
    """
    esb接口
    """


    def setUp(self):
        """
        测试类的构造方法
        该方法会在每个case运行前被调用一次
        """
        # 创建全局的接口调用类对象
        self.api_route = ApiRoute()
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

    def test_esb(self):
        """
        esb请求
        """
        time_order = int(round(time.time() * 1000))
        body_data = {
                    "assurerNo": "S36025528",
                    "sign": "",
                    "bankType": "ICBC",
                    "busiCode": "0000",
                    "platNo": "platNo",
                    "data": {
                        "pub": {
                            "bankCode": "0180400023",
                            "assurerNo": time_order,
                            "platNo": "platNo",
                            "orderNo": "ESB1706989",
                            "bankType": "ICBC",
                            "productType": "1"
                        },
                        "req": {
                            "intentionPrice": "320000",
                            "carType": "0",
                            "businessModel": "9",
                            "lender": {
                                "loanMoney": 50000.00,
                                "repayPeriod": 12,
                                "cocomNo":"shkjdw",
                                "familyAddress": "四川省屏山县新安镇场镇",
                                "endDate":"2022.07.14",
                                "bankCardNo": "4323421313213123124",
                                "idCard": "445202198102258018",
                                "phoneNum": "17610226999",
                                "signMode": "2",
                                "issueAuthority": "屏山县公安局",
                                "userName": "程阳",
                                "pics": [{
                                        "picFileName": "20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg",
                                        "picAddress": "http://hrfax.oss-cn-hangzhou.aliyuncs.com/web/2019/vxdb014020190605110243922/20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg?x-oss-process=style/carloan",
                                        "picId": 322245218,
                                        "picCode": "sfzzm"
                                    },
                                    {
                                        "picFileName": "20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg",
                                        "picAddress": "http://hrfax.oss-cn-hangzhou.aliyuncs.com/web/2019/vxdb014020190605110243922/20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg?x-oss-process=style/carloan",
                                        "picId": 322245217,
                                        "picCode": "zxsqs"
                                    },
                                    {
                                        "picFileName": "20190605-1105-2557-e0ae6a0a-6f59-8969-f567-a4e96bba5a9b.jpg",
                                        "picAddress": "http://hrfax.oss-cn-hangzhou.aliyuncs.com/web/2019/vxdb014020190605110243922/20190605-1105-2557-e0ae6a0a-6f59-8969-f567-a4e96bba5a9b.jpg?x-oss-process=style/carloan",
                                        "picId": 322245216,
                                        "picCode": "sfzfm"
                                    },
                                    {
                                        "picFileName": "20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg",
                                        "picAddress": "http://hrfax.oss-cn-hangzhou.aliyuncs.com/web/2019/vxdb014020190605110243922/20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg?x-oss-process=style/carloan",
                                        "picId": 322245216,
                                        "picCode": "rlzmz"
                                    }
                                ],
                                "startDate": "2012.04.19"
                            },
                            "downloadMode": 1,
                            "spouse": [
                            {
                                "familyAddress": "四川省屏山县新安镇场镇",
                                "endDate": "2022.04.19",
                                "bankCardNo": "4323421313213123124",
                                "idCard": "441223197205120832",
                                "phoneNum": "15122321313",
                                "issueAuthority": "屏山县公安局",
                                "userName": "杨石强",
                                "userRelationship": 3,
                                "pics": [{
                                        "picFileName": "20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg",
                                        "picAddress": "http://hrfax.oss-cn-hangzhou.aliyuncs.com/web/2019/vxdb014020190605110243922/20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg?x-oss-process=style/carloan",
                                        "picId": 322245218,
                                        "picCode": "sfzzm"
                                    },
                                    {
                                        "picFileName": "20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg",
                                        "picAddress": "http://hrfax.oss-cn-hangzhou.aliyuncs.com/web/2019/vxdb014020190605110243922/20190605-1105-3314-359271e8-863a-a324-2a61-6943ca096e4c.jpg?x-oss-process=style/carloan",
                                        "picId": 322245217,
                                        "picCode": "zxsqs"
                                    },
                                    {
                                        "picFileName": "20190605-1105-2557-e0ae6a0a-6f59-8969-f567-a4e96bba5a9b.jpg",
                                        "picAddress": "http://hrfax.oss-cn-hangzhou.aliyuncs.com/web/2019/vxdb014020190605110243922/20190605-1105-2557-e0ae6a0a-6f59-8969-f567-a4e96bba5a9b.jpg?x-oss-process=style/carloan",
                                        "picId": 322245216,
                                        "picCode": "sfzfm"
                                    }
                                ],
                                "startDate": "2012.04.19"
                            }]
                        }
                    }
                }
        # 2.调用接口
        response = self.api_route.esb_encrypt(body_data=body_data)
        # 3.获取响应数据，判断状态码，并获取“data”
        msg = "success"
        code = 0
        # 将返回解析后转换成dict的data数据
        # 若返回值不符合期望的状态码，message指明错误类型
        data_dec = self.restful.parse_response_text(response, code, msg)


        # 4.设置数据并在内部验证完整性
        DataResEsb(data_dec)
        print("test_esb pass")
        return data_dec

    # 短融ESB转发南方机构进件到E分期
    def test_route(self):
        data_json = self.test_esb()
        data1 = data_json["data"]["data"]
        sign2 = data_json["data"]["sign"]
        body_data = {

                "assurerNo": "D36024345",
                "bankType": "ICBC",
                "busiCode": "1001",
                "data":data1,
                "sign":sign2,
                "platNo": "nanfang"
        }
        response = self.api_route.route(body_data=body_data,headers=None)
        # 返回值转化成json格式
        response_json=response.json()
        # 提取E分期订单号
        OrderNo = response_json["data"]["estageOrderNo"]
        print(OrderNo)
        print("订单号success")
        return OrderNo




