from hamcrest import *


class BaseResData(object):
    def assert_code_and_print_data(self, response, code):
        assert_that(response["code"], equal_to(code))
        print(response["data"])
