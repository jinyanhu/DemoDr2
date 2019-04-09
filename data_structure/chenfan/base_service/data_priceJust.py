__author__ = 'zzh'

from hamcrest import *
import data_structure.unity as unity
from data_structure.chenfan.base import BaseData


"""
一、body或url参数形式
1.在__init__()中初始化参数
- 对于传入的参数：使用unity.copy_dict()方法，可以根据有传入的参数列表自动初始化该数据
- 需要初始化哪个参数就传哪个，显示指定参数名
- 使用示例：
    s3_body_data = S3BodyData(name=s3_name, env=s3_env)
2.使用get()方法获取设置后的dict类型数据
注：字段名需要与接口中的参数名一模一样，这样便于使用

二、接口返回的数据（如：S3Data）
用于判断数据结构、与期望值做比对
"""


# ------------------------------- 请求参数 -------------------------------- #

class DataPriceJustAdd(BaseData):
    """
    存货调价单参数构建
    """
    def __init__(self, factoryQuote=None, inventoryCode=None, inventoryId=None, productCode=None, remark=None,
                 taxRate=None, taxUnitPrice=None, unitPrice=None, vendorCode=None, vendorId=None, cmakeTime=None, createBy=None, createName=None, ddate=None, maker=None, priceJustCode=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        参数
        factoryQuote：	工厂报价
        inventoryCode：存货编码
        inventoryId：存货编码主键
        productCode：货号
        remark：调价原因
        taxRate：税率
        taxUnitPrice：含税单价
        unitPrice：无税单价
        vendorCode：供应商编码
        vendorId：供应商主键ID
        cmakeTime：制单时间
        createBy：创建人登录名称
        createName：创建人名称
        ddate：单据日期
        maker：制单人
        priceJustCode：调价单号
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResPriceJustAdd(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


class DataPriceJustDetail(BaseData):
    """
    存货调价单详情构建
    """
    def __init__(self, priceJustCode=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        参数
        priceJustCode：	调价单单号
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResPriceJustDetail(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"][0], has_key('detailList'))
        assert_that(data["obj"][0]["detailList"][0], has_key('inventoryCode'))
        assert_that(data["obj"][0]["detailList"][0], has_key('taxRate'))


# ------------- 响应值：BaseResData -------------- #
class DataResPriceJustDetail1(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"], equal_to([]))


class DataResPriceJustDetail2(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


class DataPriceJustList(BaseData):
    """
    存货调价单列表构建
    """
    def __init__(self, brandName=None, createDateEnd=None, createDateStart=None, inventoryCode=None, pageNum=None, pageSize=None, priceJustCode=None, state=None, vendorId=None, vendorName=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        参数
        brandName：品牌名
        createDateEnd：	创建日期终点
        createDateStart: 创建日期-起点
        inventoryCode：存货编码
        pageNum：页码
        pageSize：每页条数
        priceJustCode：调价单号
        state：状态
        vendorId：供应商ID
        vendorName：供应商名称
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResPriceJustList(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"], has_key('list'))
        assert_that(data["obj"]["list"][0], has_key('brandName'))
        assert_that(data["obj"]["list"][0], has_key('inventoryCode'))


class DataResPriceJustListError(object):
    """
    反例的返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
        assert_that(data, has_key('obj'))
        assert_that(data["obj"], has_key('list'))
        assert_that(data["obj"]["list"], equal_to([]))


class DataPriceJustUpdateState(BaseData):
    """
    存货调价单审核
    """
    def __init__(self, priceJustCodes=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        参数
        priceJustCode：调价单号
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResPriceJustUpdateState(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


class DataPriceJustConfirm(BaseData):
    """
    存货调价单确认
    """
    def __init__(self, priceJustCodes=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        参数
        priceJustCode：调价单号
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResPriceJustConfirm(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))


class ExportPrinceJust(BaseData):
    """
    调价单导出参数构建
    """
    def __init__(self, brandName=None, createDateEnd=None, createDateStart=None, inventoryCode=None, pageNum=None,
                 pageSize=None, state=None, vendorName=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        必填项参数
        brandName：品牌名
        createDateEnd：	创建日期终点
        createDateStart: 创建日期-起点
        inventoryCode：存货编码
        pageNum：页码
        pageSize：每页条数
        priceJustCode：调价单号
        state：状态
        vendorId：供应商ID
        vendorName：供应商名称
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class DataPriceJustUpdate(BaseData):
    """
    存货调价单修改参数构建
    """
    def __init__(self, state=None, brandId=None, brandName=None, color=None, factoryQuote=None, inventoryCode=None, inventoryId=None, isDelete=None, priceJustCode=None, priceJustDetailId=None, priceJustId=None, productCode=None, remark=None,
                 taxRate=None, taxUnitPrice=None, unitPrice=None, vendorCode=None, vendorId=None, updateBy=None, updateName=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        参数
        factoryQuote：	工厂报价
        inventoryCode：存货编码
        inventoryId：存货编码主键
        isDelete: 是否删除
        priceJustCode：存货调价单号
        priceJustDetailId：主键
        priceJustId：供应商存货调价单主表id
        productCode：货号
        remark：调价原因
        taxRate：税率
        taxUnitPrice：含税单价
        unitPrice：无税单价
        vendorCode：供应商编码
        vendorId：供应商主键ID
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResPriceJustUpdate(object):
    """
    返回值验证
    """
    def __init__(self, data, data_req=None):
        """
        初始化，获取格式化后的账户数据
        data 为账户信息，dict类型，若还是json类型，则先行转换为dict；
        data_req 为创建账户时输入的信息，dict类型（可选）
        """
        # 1.断言数据的完整性
        assert_that(data, has_key('code'))
        assert_that(data, has_key('message'))
