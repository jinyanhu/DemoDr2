from hamcrest import *
import json
import codecs


class AssertGetBaAreaResponseData(object):

    def assert_get_ba_area_ok(self, response, area_id, area_name):
        except_code = "200"
        error_msg = "状态码错误"
        assert_that(response["code"], equal_to(except_code), error_msg)

        data = codecs.decode(response["data"], "unicode_escape")
        dict_data = json.loads(data)
        assert_that(dict_data["areaId"], equal_to(area_id))
        assert_that(dict_data["areaName"], equal_to(area_name))
        assert_that(dict_data, has_key("nextLevelAreaList"))
        for list_item in dict_data["nextLevelAreaList"]:
            assert_that(list_item, has_key("areaNameEn"))
            assert_that(list_item["parentAreaId"], equal_to(area_id))
            assert_that(list_item, has_key("nextLevelAreaList"))
            assert_that(list_item, has_key("areaType"))
            assert_that(list_item, has_key("areaId"))
            assert_that(list_item, has_key("areaName"))
