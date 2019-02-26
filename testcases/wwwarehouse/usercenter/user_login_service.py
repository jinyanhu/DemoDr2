import unittest
from pyhessian.data_types import long
from api_call.wwwarehouse.usercenter.user_login_service import UserLoginService
from data_structure.wwwarehouse.usercenter.user_login_service import UserLoginServiceResData

__author__ = "zzh"


class TestUserRegisterService(unittest.TestCase):
    def setUp(self):
        self.user_login_service = UserLoginService()
        self.user_login_service_res_data = UserLoginServiceResData()

    def test_account_lock_ok(self):
        """
        账号锁定
        :return:
        """
        mobile = "18888888888"
        lock_type = "lock"
        lock_reason = "dubbo测试锁定账号"
        operator_user_id = "16100603956"
        response = self.user_login_service.account_lock(mobile, lock_type, lock_reason, operator_user_id)
        self.user_login_service_res_data.assert_account_lock_ok(response)

        # 解锁
        lock_type = "unlock"
        lock_reason = "dubbo解锁账号"
        self.user_login_service.account_lock(mobile, lock_type, lock_reason, operator_user_id)

    def test_account_unlock_ok(self):
        """
        账号解锁
        :return:
        """
        # 锁定账号
        mobile = "18888888888"
        lock_type = "lock"
        lock_reason = "dubbo锁定账号"
        operator_user_id = "16100603956"
        try:
            self.user_login_service.account_lock(mobile, lock_type, lock_reason, operator_user_id)
        except Exception as e:
            pass

        lock_type = "unlock"
        lock_reason = "dubbo测试解锁账号"
        response = self.user_login_service.account_lock(mobile, lock_type, lock_reason, operator_user_id)
        self.user_login_service_res_data.assert_account_unlock_ok(response)

    # def test_check_scan_code_ok(self):
    #     """
    #     验证手机端扫的二维码
    #     :return:
    #     """
    #     token = ""
    #     user_id = 1
    #     security_query_code = ""
    #     response = self.user_login_service.check_scan_code(token, user_id, security_query_code)
    #     self.user_login_service_res_data.assert_check_scan_code_ok(response)

    def test_get_account_lock_locked_ok(self):
        """
        账号锁定时，获取账号锁定情况
        :return:
        """
        # 锁定账号
        mobile = "18888888888"
        lock_type = "lock"
        lock_reason = "dubbo锁定账号"
        operator_user_id = "16100603956"
        try:
            self.user_login_service.account_lock(mobile, lock_type, lock_reason, operator_user_id)
        except Exception as e:
            pass

        account = "18888888888"
        response = self.user_login_service.get_account_lock(account)
        try:
            self.user_login_service_res_data.assert_get_account_lock_locked_ok(response)
        except Exception as e:
            raise

        finally:
            # 解锁
            lock_type = "unlock"
            lock_reason = "dubbo解锁账号"
            self.user_login_service.account_lock(mobile, lock_type, lock_reason, operator_user_id)

    def test_get_account_lock_unlocked_ok(self):
        """
        账号未锁定时，获取账号锁定情况
        :return:
        """
        # 前提：账号解锁
        mobile = "18888888888"
        lock_type = "unlock"
        lock_reason = "dubbo解锁"
        operator_user_id = "16100603956"
        try:
            self.user_login_service.account_lock(mobile, lock_type, lock_reason, operator_user_id)
        except Exception as e:
            pass

        account = "18888888888"
        response = self.user_login_service.get_account_lock(account)
        self.user_login_service_res_data.assert_get_account_lock_unlocked_ok(response)

    def test_get_cm_user_by_user_id_ok(self):
        """
        根据userId获取用户信息
        :return:
        """
        user_id = 16100603956
        response = self.user_login_service.get_cm_user_by_user_id(user_id)
        self.user_login_service_res_data.assert_get_cm_user_by_user_id_ok(response, user_id)

    def test_get_cm_user_by_mobile_ok(self):
        """
        根据mobile获取用户信息
        :return:
        """
        mobile = "18888888888"
        response = self.user_login_service.get_cm_user_by_mobile(mobile)
        self.user_login_service_res_data.assert_get_cm_user_by_mobile_ok(response, mobile)

    def test_get_verification_ok(self):
        """
        获取图片验证码
        :return:
        """
        device_info = "122324345"
        response = self.user_login_service.get_verification(device_info)
        self.user_login_service_res_data.assert_get_verification_ok(response)

    def test_insert_cm_login_log_ok(self):
        """
        插入日志
        :return:
        """
        cm_login_log_dict = {
            "clientIp": "192.168.100.200",
            "createTime": "2017-07-13",
            "createUserId": long(16100603956),
            "deviceInfo": "1223243223",
            "deviceMac": "4C:FB:45:D6:F1:90",
            "deviceType": "a",
            "eventType": 0,
            "identifyType": 0,
            "isSuccess": 0,
            "loginUkid": "",
            "message": "dubbo测试插入日志",
            "serialVersionUID": "",
            "updateTime": "2017-07-13",
            "updateUserId": long(16100603956),
            "userId": long(16100603956)
        }
        response = self.user_login_service.insert_cm_login_log(cm_login_log_dict)
        self.user_login_service_res_data.assert_insert_cm_login_log_ok(response)

    def test_is_mobile_platform_ok(self):
        """
        平台是否移动平台
        :return:
        """
        platform = "a"
        response = self.user_login_service.is_mobile_platform(platform)
        self.user_login_service_res_data.assert_is_mobile_platform_ok(response)

    def test_is_valid_platform_ok(self):
        """
        是否合法的平台
        :return:
        """
        platform = "iq"
        response = self.user_login_service.is_valid_platform(platform)
        self.user_login_service_res_data.assert_is_valid_platform_ok(response)

    # def test_login_bind_ok(self):
    #     """
    #     绑定设备
    #     :return:
    #     """
    #     mobile = "18888888888"
    #     response = self.user_login_service.login_bind(mobile)
    #     self.user_login_service_res_data.assert_login_bind_ok(response)

    # def test_login_confirm_ok(self):
    #     """
    #     手机端确认登录
    #     :return:
    #     """
    #     user_id = ""
    #     security_query_code = ""
    #     response = self.user_login_service.login_confirm(user_id, security_query_code)
    #     self.user_login_service_res_data.assert_login_confirm_ok(response)

    # def test_login_out_ok(self):
    #     """
    #     登出
    #     :return:
    #     """
    #     user_id = ""
    #     token = ""
    #     device_type = ""
    #     response = self.user_login_service.login_out(user_id, token, device_type)
    #     self.user_login_service_res_data.assert_login_out_ok(response)

    # def test_scan_account_ok(self):
    #     """
    #     PC端轮询获取用户账号
    #     :return:
    #     """
    #     security_query_code = ""
    #     user_ip = ""
    #     response = self.user_login_service.scan_account(security_query_code, user_ip)
    #     self.user_login_service_res_data.assert_scan_account_ok(response)

    def test_scan_code_ok(self):
        """
        PC端请求二维码
        :return:
        """
        response = self.user_login_service.scan_code()
        self.user_login_service_res_data.assert_scan_code_ok(response)
    #
    # def test_update_device_token_ok(self):
    #     """
    #     更新deviceToken
    #     :return:
    #     """
    #     token = ""
    #     device_token = ""
    #     user_id = 11
    #     response = self.user_login_service.update_device_token(token, device_token, user_id)
    #     self.user_login_service_res_data.assert_update_device_token_ok(response)

    def test_update_password_ok(self):
        """
        修改密码
        :return:
        """
        mobile = "18888888888"
        password = "a123456"
        client_ip = "192.168.10.120"

        password_response = self.user_login_service.get_encrypt_password(password)
        new_password = password_response["data"]

        response = self.user_login_service.update_password(mobile, new_password, client_ip)
        self.user_login_service_res_data.assert_update_password_ok(response)

