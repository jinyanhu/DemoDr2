from api_call.wwwarehouse.base import BaseHessian
from cof.hessian_util import *
from pyhessian import protocol
from pyhessian.data_types import long

__author__ = "zzh"


class UserLoginService(BaseHessian):
    def __init__(self):
        BaseHessian.__init__(self)
        self.base_url = "http://192.168.200.98:9091/"
        url = self.base_url + "com.wwwarehouse.xdw.usercenter.service.UserLoginService"
        self.hessian = HessianUtil(api_url=url)

    def account_lock(self, mobile, lock_type, lock_reason, operator_user_id):
        """
        账号锁定解锁
        :return:
        """
        method = "accountLock"
        operator_user_id = long(operator_user_id)
        response = self.hessian.request(method, mobile, lock_type, lock_reason, operator_user_id)
        return response

    def check_scan_code(self, token, user_id, security_query_code):
        """
        验证手机端扫的二维码
        :param token:
        :param user_id:
        :param security_query_code:
        :return:
        """
        method = "checkScanCode"
        user_id = long(user_id)
        response = self.hessian.request(method, token, user_id, security_query_code)
        return response

    def get_account_lock(self, account):
        """
        获取账号锁定情况
        :param account:
        :return:
        """
        method = "getAccountLock"
        response = self.hessian.request(method, account)
        return response

    def get_cm_user_by_user_id(self, user_id):
        """
        根据userId获取用户信息
        :param user_id:
        :return:
        """
        method = "getCmUserByUserId"
        user_id = long(user_id)
        response = self.hessian.request(method, user_id)
        return response

    def get_cm_user_by_mobile(self, mobile):
        """
        根据手机号获取用户
        :param mobile:
        :return:
        """
        method = "getCmUserByMobile"
        response = self.hessian.request(method, mobile)
        return response

    def get_verification(self, device_info):
        """
        获取图片验证码
        :param device_info:
        :return:
        """
        method = "getVerification"
        response = self.hessian.request(method, device_info)
        return response

    def insert_cm_login_log(self, cm_login_log_dict):
        """
        插入日志
        :param cm_login_log_dict:
        :return:
        """
        method = "insertCmLoginLog"
        cm_login_log = protocol.object_factory("com.wwwarehouse.xdw.usercenter.model.CmLoginLog", cm_login_log_dict)
        response = self.hessian.request(method, cm_login_log)
        return response

    def is_mobile_platform(self, platform):
        """
        平台是否移动平台
        :param platform:
        :return:
        """
        method = "isMobilePlatform"
        response = self.hessian.request(method, platform)
        return response

    def is_valid_platform(self, platform):
        """
        是否合法的平台
        :param platform:
        :return:
        """
        method = "isValidPlatform"
        response = self.hessian.request(method, platform)
        return response

    def login_bind(self, mobile):
        """
        绑定设备
        :param mobile:
        :return:
        """
        method = "loginBind"
        response = self.hessian.request(method, mobile)
        return response

    def login_confirm(self, user_id, security_query_code):
        """
        手机端确认登录
        :return:
        """
        method = "loginConfirm"
        user_id = long(user_id)
        response = self.hessian.request(method, user_id, security_query_code)
        return response

    def login_out(self, user_id, token, device_type):
        """
        登出
        :return:
        """
        method = "loginOut"
        user_id = long(user_id)
        response = self.hessian.request(method, user_id, token, device_type)
        return response

    def scan_account(self, security_query_code, user_ip):
        """
        PC端轮询获取用户账号
        :return:
        """
        method = "scanAccount"
        response = self.hessian.request(method, security_query_code, user_ip)
        return response

    def scan_code(self):
        """
        PC端请求二维码
        :return:
        """
        method = "scanCode"
        response = self.hessian.request(method)
        return response

    def update_device_token(self, token, device_token, user_id):
        """
        更新deviceToken
        :return:
        """
        method = "updateDeviceToken"
        user_id = long(user_id)
        response = self.hessian.request(method, token, device_token, user_id)
        return response

    def update_password(self, mobile, password, client_ip):
        """
        修改密码
        :return:
        """
        method = "updatePassword"
        response = self.hessian.request(method, mobile, password, client_ip)
        return response

    def get_encrypt_password(self, password):
        """
        获取加密密码
        :param password:
        :return:
        """
        method = "getEncryptPassword"
        response = self.hessian.request(method, password)
        return response







