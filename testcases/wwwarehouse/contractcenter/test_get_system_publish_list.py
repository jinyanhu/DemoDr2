import unittest
from api_call.wwwarehouse.contractcenter_service.pb_resource_service import *


class TestGetSystemPublishList(unittest.TestCase):
    def setUp(self):
        self.pb_resource_service = PbResourceService()

    def test_get_system_publish_list_ok(self):
        businessUkid = 0
        seeAbleBusinessUkid = 0
        rsId = 0
        response = self.pb_resource_service.get_system_publish_list(businessUkid, seeAbleBusinessUkid, rsId)
        print(response)
