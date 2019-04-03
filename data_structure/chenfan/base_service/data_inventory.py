
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
    获取尺码分类信息
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


class GetStyleInfo(BaseData):
    """
    获取款式来源
    """
    def __init__(self):
        """
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResGetStyleInfo(object):
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
        assert_that(data['obj'][0], has_key('code'))
        assert_that(data['obj'][0], has_key('name'))


class ResAddInventory(object):

    def __init__(self, data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


class EditInventory(BaseData):
    """
    存货档案更新接口
    """
    def __init__(self, barcode=None, brandId=None, brandName=None, color=None, composition=None, compositionName=None,
                       createBy=None, createDate=None, createName=None, implementationStandards=None, invCCode=None,
                       invCCode1=None, invCName=None, inventoryCategory=None, inventoryClassId=None, inventoryCode=None,
                       inventoryId=None, inventoryName=None, level=None, newDate=None, procodeCover=None, procodeImgs=None,
                       productCode=None, safetyTechnology=None, season=None, size=None, state=None, styleSource=None,
                       wmcategory=None):
        """
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResEditInventory(object):

    def __init__(self, data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


class GetInventoryList(BaseData):
    """
    获取存货档案列表
    """
    def __init__(self, brandId=None, invCName=None, inventoryCode=None, isCraftsId=None, pageSize=None, pageNum=None,
                       total=None, newDateBegin=None, newDateEnd=None, productCode=None):

        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResGetInventoryList(object):

    def __init__(self, data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        if data['obj']['list']:
            assert_that(data['obj']['list'][0], has_key('productCode'))
            assert_that(data['obj']['list'][0], has_key('inventoryCode'))
            assert_that(data['obj']['list'][0], has_key('invCName'))
            assert_that(data['obj']['list'][0], has_key('brand'))
        else:
            pass


class GetInventoryInfo(BaseData):
    """
    获取存货档案详情
    """
    def __init__(self, productCode=None, state=None):

        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResGetInventoryInfo(object):

    def __init__(self, data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        try:
            assert_that(data, has_key('obj'))
            assert_that(data['obj'], has_key('productCode'))
            assert_that(data['obj'], has_key('newDate'))
            assert_that(data['obj'], has_key('invCCode'))
            assert_that(data['obj'], has_key('brandName'))
        except AssertionError:
            pass


class ExportInventoryQualified(BaseData):
    """
    按合格证模板导出
    """
    def __init__(self, brandId=None, invCName=None, inventoryCode=None, isCraftsId=None, pageSize=None, pageNum=None,
                       total=None, newDateBegin=None, newDateEnd=None, productCode=None):
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ExportInventory(BaseData):
    """
    存货档案导出
    """
    def __init__(self, brandId=None, invCName=None, inventoryCode=None, isCraftsId=None, pageSize=None, pageNum=None,
                       total=None, newDateBegin=None, newDateEnd=None, productCode=None):
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class SwitchState(BaseData):
    """
    启用禁用存货档案
    """
    def __init__(self, inventoryIds=None, state=None):
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class ResSwitchState(object):
    """
    验证接口返回数据
    """
    def __init__(self, data):
        """
        初始化，获取格式化后的数据
        :param data:
        """
        # 断言数据的正确性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))