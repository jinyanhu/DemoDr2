from hamcrest import *

from data_structure.chenfan.base import BaseResData

__author__ = "zzh"


class UserRegisterServiceResData(BaseResData):
    def __init__(self):
        pass

    def assert_check_in_card_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_check_image_code_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_check_invite_code_ok(self, response):
        self.assert_code_and_print_data(response, 200)
        data = response["data"]
        assert_that(data, equal_to(True))

    def assert_check_register_result_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_create_invite_link_ok(self, response):
        self.assert_code_and_print_data(response, 200)

    def assert_receive_register_info_ok(self, response):
        self.assert_code_and_print_data(response, 200)

