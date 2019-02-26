from hamcrest import *
import json
import codecs
from data_structure.base import BaseResData

__author__ = "zzh"


class UserLoginServiceResData(BaseResData):
    def __init__(self):
        pass

    def assert_account_lock_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_account_unlock_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_check_scan_code_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_get_account_lock_locked_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_get_account_lock_unlocked_ok(self, response):
        self.assert_code_and_print_data(response, 500)

    def assert_get_cm_user_by_user_id_ok(self, response, user_id):
        self.assert_code_and_print_data(response, 200)
        data = response["data"]
        data_json = json.loads(data)

        assert_that(data_json, has_key("createTime"))
        assert_that(data_json, has_key("createUserId"))
        assert_that(data_json, has_key("faceUkid"))
        assert_that(data_json, has_key("lastLoginFailTime"))
        assert_that(data_json, has_key("lockedTime"))
        assert_that(data_json, has_key("lockReason"))
        assert_that(data_json, has_key("mobile"))
        assert_that(data_json, has_key("password"))
        assert_that(data_json, has_key("passwordErrorTimes"))
        assert_that(data_json, has_key("passwordUpdateTime"))
        assert_that(data_json, has_key("registeIp"))
        assert_that(data_json, has_key("registeMac"))
        assert_that(data_json, has_key("registeTime"))
        assert_that(data_json, has_key("status"))
        assert_that(data_json, has_key("updateTime"))
        assert_that(data_json, has_key("updateUserId"))
        assert_that(data_json, has_key("userId"))

        assert_that(data_json["userId"], equal_to(str(user_id)))

    def assert_get_cm_user_by_mobile_ok(self, response, mobile):
        self.assert_code_and_print_data(response, 200)
        data = response["data"]
        data_json = json.loads(data)

        assert_that(data_json, has_key("createTime"))
        assert_that(data_json, has_key("createUserId"))
        assert_that(data_json, has_key("faceUkid"))
        assert_that(data_json, has_key("lastLoginFailTime"))
        assert_that(data_json, has_key("lockedTime"))
        assert_that(data_json, has_key("lockReason"))
        assert_that(data_json, has_key("mobile"))
        assert_that(data_json, has_key("password"))
        assert_that(data_json, has_key("passwordErrorTimes"))
        assert_that(data_json, has_key("passwordUpdateTime"))
        assert_that(data_json, has_key("registeIp"))
        assert_that(data_json, has_key("registeMac"))
        assert_that(data_json, has_key("registeTime"))
        assert_that(data_json, has_key("status"))
        assert_that(data_json, has_key("updateTime"))
        assert_that(data_json, has_key("updateUserId"))
        assert_that(data_json, has_key("userId"))

        assert_that(data_json["mobile"], equal_to(mobile))

    def assert_get_verification_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_insert_cm_login_log_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_is_mobile_platform_ok(self, response):
        self.assert_code_and_print_data(response, 200)
        data = response["data"]
        assert_that(data, equal_to("True"))

    def assert_is_valid_platform_ok(self, response):
        self.assert_code_and_print_data(response, 200)
        data = response["data"]
        assert_that(data, equal_to("True"))

    def assert_login_bind_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_login_confirm_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_login_out_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_scan_account_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_scan_code_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_update_device_token_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_update_password_ok(self, response):
        self.assert_code_and_print_data(response, 200)
