

from hamcrest import *
import data_structure.unity as unity
from data_structure.chenfan.base import BaseData


class DataBrand(BaseData):
    """
    品牌列表接口参数构建
    """
    def __init__(self,brandCode=None, brandName=None, pageNum=None, pageSize=None, state=None):
        """
        :param brandCode:
        :param brandName:
        :param pageNum:
        :param pageSize:
        :param state:
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class DataResBrand(object):
    """
    验证返回数据
    """
    def __init__(self,data):
        """
        初始化，获取格式化后的账户数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"], has_key('list'))
        assert_that(data["obj"]["list"][0], has_key('brandId'))
        assert_that(data["obj"]["list"][0], has_key('brandCode'))
        assert_that(data["obj"]["list"][0], has_key('brandName'))
        assert_that(data["obj"]["list"][0], has_key('brandType'))


class DataResBrandFailure(object):

    """
    验证反例的返回数据
    """
    def __init__(self, data):
        """
        初始化，获取格式化后的账户数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"]["list"], equal_to([]))


class DataCreateBrand(BaseData):
    """
    品牌创建接口
    """
    def __init__(self, brandCode=None, brandName=None, brandType=None, createBy=None, createName=None, customerId=None,
                 customerName=None,magnification=None, prefixEn=None, receiveAddress=None, receiveName=None,
                 receiveTel=None, state=None, lowestOnTimeReachScore=None, lowestPerformanceScore=None,
                 lowestPostSaleDefectiveScore=None,lowestPreSaleDefectiveScore=None, lowestReOrderPeriodScore=None,
                 lowestVendorLevel=None):
        """
        接口数据初始化
        :param brandCode: 品牌编码
        :param brandName: 品牌名称
        :param brandType: 品牌类型
        :param createBy: 创建人ID
        :param createName: 创建人名称
        :param customerId: 客户ID
        :param customerName: 客户名
        :param magnification: 倍率
        :param prefixEn: 前缀
        :param receiveAddress:收货地址
        :param receiveName: 收货人
        :param receiveTel: 联系方式
        :param state: 状态
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class DataResCreateBrand(object):

    def __init__(self, data):
        """
        初始化，获取格式化后的账户数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


class DataEditBrand(BaseData):
    """
    品牌修改接口
    """
    def __init__(self, brandCode=None, brandName=None, brandType=None, createBy=None, createName=None, customerId=None,
                 customerName=None,magnification=None, prefixEn=None, receiveAddress=None, receiveName=None,
                 receiveTel=None, state=None, lowestOnTimeReachScore=None, lowestPerformanceScore=None,
                 lowestPostSaleDefectiveScore=None,lowestPreSaleDefectiveScore=None, lowestReOrderPeriodScore=None,
                 lowestVendorLevel=None, updateBy=None, updateName=None,brandId=None):
        """
        接口数据初始化
        :param brandCode: 品牌编码
        :param brandName: 品牌名称
        :param brandType: 品牌类型
        :param createBy: 创建人ID
        :param createName: 创建人名称
        :param customerId: 客户ID
        :param customerName: 客户名
        :param magnification: 倍率
        :param prefixEn: 前缀
        :param receiveAddress:收货地址
        :param receiveName: 收货人
        :param receiveTel: 联系方式
        :param state: 状态
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class DataResEditBrand(object):

    def __init__(self, data):
        """
        初始化，获取格式化后的账户数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


