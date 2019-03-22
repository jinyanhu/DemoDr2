
import json
from utils.http_util import Http
from api_call.chenfan.base import BaseHttp
from api_call.chenfan.login.api_login import ApiLogin


class ApiBrand(BaseHttp):
    """
    品牌列表接口
    """
    def __init__(self):

        BaseHttp.__init__(self)
        self.api_login = ApiLogin()
        self.api_login.set_admin_login_header(self.header)  # 加登录header
        self.http = Http(self.header)  # http对象

    def get_brand_list(self,body_data=None):
        """
        获取全部品牌列表
        :return:
        """
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_code_brand_list(self, body_data=None):
        """
        根据品牌编码获取品牌列表
        :return:
        """
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_code_brand_list_failure(self, body_data=None):
        """
        根据不存在的品牌编码获取品牌列表
        :return:
        """
        # 参数字段创建
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_name_brand_list(self, body_data=None):
        """
        根据品牌名称获取品牌列表
        :return:
        """
        # 参数字段创建
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_name_brand_list_nothing(self, body_data=None):
        """
        根据不存在的品牌名称获取品牌列表
        :return:
        """
        # 参数字段创建
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_state_brand_list_enable(self, body_data=None):
        """
        根据品牌启用状态获取品牌列表
        :return:
        """
        # 参数字段创建
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def get_state_brand_list_disable(self, body_data=None):
        """
        根据品牌禁用状态获取品牌列表
        :return:
        """
        # 参数字段创建
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/getList"
        # 请求品牌列表接口得到返回值
        response = self.http.get(url=url, params=body_data)
        return response

    def create_brand(self, body_data=None):
        """
        正常创建品牌
        :param body_data: 字典，包含创建品牌的所有字段
        :return:
        """
        if body_data:
            body_data = body_data.get()
        # 请求的地址
        url = self.url + "/chenfan_base/brand/add"
        # 请求品牌列表接口得到返回值
        response = self.http.post(url=url, body=body_data)
        return response
