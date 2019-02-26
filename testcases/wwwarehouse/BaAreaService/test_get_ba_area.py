import unittest
from api_call.wwwarehouse.BaAreaService.get_ba_area import *
from data_structure.wwwarehouse.BaAreaService.assert_get_ba_area import *


class TestGetBaArea(unittest.TestCase):
    def setUp(self):
        self.getBaArea = GetBaArea()
        self.assert_get_ba_area_response = AssertGetBaAreaResponseData()

    def tearDown(self):
        pass

    def test_get_ba_area_ok(self):
        area_id = "110100"
        area_name = "北京市"
        response = self.getBaArea.request(area_id, area_name)

        self.assert_get_ba_area_response.assert_get_ba_area_ok(response, area_id, area_name)

