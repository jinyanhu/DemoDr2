
from hamcrest import *
import data_structure.unity as unity
from data_structure.chenfan.base import BaseData


class GetBrandList(BaseData):
    """
    获取品牌信息接口类
    """
    def __init__(self, brandid=None, brandname=None,state=None):
        """

        :param brandid: 品牌id
        :param brandname: 品牌名称
        :param state: 状态
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResGetBrandList(object):
    """
    验证返回数据
    """
    def __init__(self,data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"][0], has_key('brandId'))
        assert_that(data["obj"][0], has_key('brandCode'))
        assert_that(data["obj"][0], has_key('brandName'))


class GetInventoryClassInfoList(BaseData):
    """
    获取存货分类编码
    """
    def __init__(self, invCCode=None, invCCode1=None, invCCode3=None, invCEnd=None, invCGrade=None, invCName=None,
                       inventoryClassId=None):
        """

        :param invCCode:
        :param invCCode1:
        :param invCCode3:
        :param invCEnd:
        :param invCGrade:
        :param invCName:
        :param inventoryClassId:
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResGetInventoryClassInfoList(object):
    """
     验证返回数据
    """
    def __init__(self, data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"][0], has_key('invCCode'))
        assert_that(data["obj"][0], has_key('invCName'))
        assert_that(data["obj"][0], has_key('inventoryClassId'))


class GetSizeSortInfoList(BaseData):
    """
    获取
    """
    def __init__(self):
        """
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResGetSizeSortInfoList(object):
    """
     验证返回数据
    """
    def __init__(self, data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data['obj'][0], has_key('createDate'))
        assert_that(data['obj'][0], has_key('size'))
        assert_that(data['obj'][0], has_key('sizeSortId'))
        assert_that(data['obj'][0], has_key('sort'))
        assert_that(data['obj'][0], has_key('updateDate'))



