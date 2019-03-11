from pyhessian import protocol
from pyhessian.data_types import long

from api_call.wwwarehouse.base import BaseHessian
from utils.hessian_util import *

__author__ = "zzh"


class UserRegisterService(BaseHessian):
    def __init__(self):
        BaseHessian.__init__(self)
        self.base_url = "http://192.168.200.98:9091/"
        url = self.base_url + "com.wwwarehouse.xdw.usercenter.service.UserRegisterService"
        self.hessian = HessianUtil(api_url=url)

    def check_in_card(self, id_card):
        """
        检测身份证
        :param id_card:
        :return:
        """
        method = "checkIdCard"
        response = self.hessian.request(method, id_card)
        return response

    def check_image_code(self, device_info, image_code):
        """
        验证图片验证码
        :param device_info:
        :param image_code:
        :return:
        """
        method = "checkImageCode"
        response = self.hessian.request(method, device_info, image_code)
        return response

    def check_invite_code(self, invite_code):
        """
        检测邀请码
        :param invite_code:
        :return:
        """
        method = "checkInviteCode"
        invite_code = long(invite_code)
        response = self.hessian.request(method, invite_code)
        return response

    def check_register_result(self, invite_code, mobile):
        """
        注册识别结果接口
        :param invite_code:
        :param mobile:
        :return:
        """
        method = "checkRegisteResult"
        response = self.hessian.request(method, invite_code, mobile)
        return response

    def create_invite_link(self, mobile, name, service_type, user_id):
        """
        生成邀请链接接口
        :param mobile:
        :param name:
        :param service_type:
        :param user_id:
        :return:
        """
        method = "createInviteLink"
        user_id = long(user_id)
        response = self.hessian.request(method, mobile, name, service_type, user_id)
        return response

    def receive_register_info(self, register_info_dict):
        """
        接收注册信息接口
        :param register_info_dict:
        :return:
        """
        method = "receiveRegisterInfo"
        register_info = protocol.object_factory("com.wwwarehouse.xdw.usercenter.model.RegisterInfo", fields=None, bases=None, attrs=None, **register_info_dict)
        register_info = protocol.object_factory("com.wwwarehouse.xdw.usercenter.model.RegisterInfo", deviceInfo="1234554321",
                                                deviceToken="2323", deviceType="a", face="/temp/ca00ce3d-84ea-4337-ab9b-79538f84cf25.jpeg", idBack="/temp/ca00ce3d-84ea-4337-ab9b-79538f84cf25.jpeg", idCard="837283842738495848",
                                                idFront="/temp/ca00ce3d-84ea-4337-ab9b-79538f84cf25.jpeg", mobile="15806011111", password="faCTtj8zRjtBCNfIxi/+gR3MEE0OR11EjSGXPgzhppCLmGTpoUPNGSDmTv2wdqQYSz3jTViB2FwFfC59jMDvJ+1ID8hAjE5wnrJK7goicb8W3jGYssUkleCQvj9LOlCaMMNBkUDtnBywBJu0LQD5bIqfNysEE6yB6hydq+z3NDk=", personName="zjh",
                                                personSex=1, registeIp="192.168.1.1", registeMac="02:23:de:ie:12",
                                                serviceType="1", unionId="12233")
        response = self.hessian.request(method, register_info)
        return response



