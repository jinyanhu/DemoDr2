

from utils.database_util import Database
from utils.http_util import Http
from api_call.chenfan.base import BaseHttp
from api_call.chenfan.login.api_login import ApiLogin


class ApiInventory(BaseHttp):
    """
    存货档案接口
    """
    def __init__(self):

        BaseHttp.__init__(self)
        self.database = Database("pymysql")
        self.api_login = ApiLogin()
        self.api_login.set_admin_login_header(self.header)  # 加登录header
        self.http = Http(self.header)

    def get_brand_list(self,body_data=None):
        """
        获取全部品牌列表
        :return:
        """
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/base/getBrandInfoList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_inventory_class_info_list(self,body_data=None):
        """
        获取全部品牌列表
        :return:
        """
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/base/getInventoryClassInfoList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_size_sort_info_list(self):
        """
        获取全部品牌列表
        :return:
        """
        # 请求的地址
        url = self.url + "/chenfan_base/base/getSizeSortInfoList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url)
        return response
