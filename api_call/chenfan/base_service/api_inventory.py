
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

    def get_brand_list(self, body_data=None):
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

    def get_inventory_class_info_list(self, body_data=None):
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

    def get_style_info(self):
        """
        获取全部品牌列表
        :return:
        """
        # 请求的地址
        url = self.url + "/chenfan_base/base/getStyleInfo"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url)
        return response

    def add_inventory(self, body_data):
        """
        存货编码新增
        :return:
        """
        # 请求的地址
        url = self.url + "/chenfan_base/inventory/add"
        # 请求品牌列表接口得到返回值
        response = self.http.post(url=url, body=body_data)
        return response

    def delete_inventory(self, sql):
        """
        数据删除方法
        :param sql: sql语句
        :return:
        """
        self.database.update(sql=sql)

    def edit_inventory(self, body_data):
        """
        存货编码更新
        :return:
        """

        # 请求的地址
        url = self.url + "/chenfan_base/inventory/update"
        # 请求品牌列表接口得到返回值
        response = self.http.put(url=url, body=body_data)
        return response

    def get_inventory_list(self, body_data):
        """
        查询存货编码列表
        :return:
        """
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/inventory/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_inventory_info(self, body_data):
        """
        查询存货编码详情
        :return:
        """
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/inventory/getInfo"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def export_inventory(self, body_data):
        """
        按合格证模板导出
        :param body_data:
        :return:
        """
        if body_data:
            body_data = body_data.get()
        url = self.url + "/chenfan_base/inventory/export"
        response = self.http.get(url=url, params=body_data)
        return response

    def export_inventory_qualified(self, body_data):
        """
        按合格证模板导出
        :param body_data:
        :return:
        """
        if body_data:
            body_data = body_data.get()
        url = self.url + "/chenfan_base/inventory/exportQA"
        response = self.http.get(url=url, params=body_data)
        return response

    def switch_state(self, body_data):
        """
        启用禁用存货档案
        :param body_data:
        :return:
        """
        if body_data:
            body_data = body_data.get()
        url = self.url + "/chenfan_base/inventory/switchState"
        response = self.http.post(url=url, body=body_data)
        return response
