from cof.hessian_util import *


class GetBaArea():
    def __init__(self):
        url = "http://192.168.6.24:9090/com.wwwarehouse.xdw.datasync.service.BaAreaService"
        self.hessian = HessianUtil(api_url=url)

    def request(self, areaId, areaName):
        method = "getBaArea"
        response = self.hessian.request(method, areaId, areaName)
        return response


