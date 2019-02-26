import unittest
from pyhessian.data_types import long
from api_call.wwwarehouse.usercenter.user_register_service import UserRegisterService
from data_structure.wwwarehouse.usercenter.user_register_service import UserRegisterServiceResData

__author__ = "zzh"


class TestUserRegisterService(unittest.TestCase):
    def setUp(self):
        self.user_register_service = UserRegisterService()
        self.user_register_service_res_data = UserRegisterServiceResData()

    def test_check_in_card_ok(self):
        """
        检测身份证
        :return:
        """
        id_card = "350525198912123049"
        response = self.user_register_service.check_in_card(id_card)
        self.user_register_service_res_data.assert_check_in_card_ok(response)

    def test_check_image_code_ok(self):
        """
        验证图片验证码
        :return:
        """
        device_info = ""
        image_code = ""
        response = self.user_register_service.check_image_code(device_info, image_code)
        self.user_register_service_res_data.assert_check_image_code_ok(response)

    def test_check_invite_code_ok(self):
        """
        检测邀请码
        :return:
        """
        invite_code = ""
        response = self.user_register_service.check_invite_code(invite_code)
        self.user_register_service_res_data.assert_check_invite_code_ok(response)

    def test_check_register_result_ok(self):
        """
        注册识别结果接口
        :return:
        """
        invite_code = ""
        mobile = ""
        response = self.user_register_service.check_register_result(invite_code, mobile)
        self.user_register_service_res_data.assert_check_register_result_ok(response)

    def test_create_invite_link_ok(self):
        """
        生成邀请链接接口
        :return:
        """
        mobile = ""
        name = ""
        service_type = "1"
        user_id = 1
        response = self.user_register_service.create_invite_link(mobile, name, service_type, user_id)
        self.user_register_service_res_data.assert_create_invite_link_ok(response)

    def test_receive_register_info_ok(self):
        """
        接收注册信息接口
        :return:
        """
        register_info_dict = {
            "deviceInfo": "1234554321",
            "deviceToken ": "123",
            "deviceType": "a",
            "face": "/temp/ca00ce3d-84ea-4337-ab9b-79538f84cf25.jpeg",
            "idBack": "/temp/ca00ce3d-84ea-4337-ab9b-79538f84cf25.jpeg",
            "idCard": "328493849583948987",
            "idFront": "/temp/ca00ce3d-84ea-4337-ab9b-79538f84cf25.jpeg",
            "mobile": "158060111111",
            "password": "a123456",
            "personName": "yjh",
            "personSex": 1,
            "registeIp": "192.168.10.211",
            "registeMac": "02:23:de:ie:12",
            "serviceType": "1",
            "unionId": "11123"
        }
        response = self.user_register_service.receive_register_info(register_info_dict)
        self.user_register_service_res_data.assert_receive_register_info_ok(response)




