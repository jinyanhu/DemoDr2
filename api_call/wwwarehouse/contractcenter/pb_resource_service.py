from cof.parser_wwarehouse_ini import *

from utils.hessian_util import *


class PbResourceService():
    def __init__(self):
        host, port = get_host_and_port()
        url = host + ":" +port +"/com.wwwarehouse.xdw.contractcenter.service.PbResourceService"
        print(url)
        self.hessian = HessianUtil(api_url=url)

    def get_system_publish_list(self, businessUkid, seeAbleBusinessUkid, rsId):
        method = "getSystemPublishList"
        response = self.hessian.request(method, businessUkid, seeAbleBusinessUkid, rsId)
        return response

    def pb_system_resource(self, rsSystemPublish):
        method = "pbSystemResource"
        response = self.hessian.request(method, rsSystemPublish)
        return response

    def resource_off_shelves(self, businessUkid, seeAbleBusinessUkid, rsId):
        method = "resourceOffShelves"
        response = self.hessian.request(method, businessUkid, seeAbleBusinessUkid, rsId)
        return response
