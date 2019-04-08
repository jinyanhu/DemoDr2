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
class DataVendorList(BaseData):
    """
    供应商列表参数构建
    """
    def __init__(self, category=None, coreproduct=None, factoryGrade=None, factorylocation=None, pageNum=None,
                 pageSize=None, state=None, venAbbName=None, vendorCode=None, vensource=None, ventype=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        参数
        name：s3账户名称
        env：环境，1:开发，2：测试，8：正式
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResVendorList(object):
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
        assert_that(data["obj"]["list"][0], has_key('vendorId'))
        assert_that(data["obj"]["list"][0], has_key('vendorCode'))
        assert_that(data["obj"]["list"][0], has_key('vendorName'))
        assert_that(data["obj"]["list"][0], has_key('venAbbName'))

        # 2.根据传入的参数，进行数据正确性断言


class DataVendorAdd(BaseData):
    """
    供应商新增参数构建
    """
    def __init__(self, accname=None, annualOutput=None, category=None, companyRegistrationTime=None, cooperativeAttribute=None,
                 cooperativePositioningcol=None, cooperativeStatus=None, coreproduct=None, cvenAccount=None, cvenAddress=None, cvenAddress2=None,
                 cvenBank=None, cvenHand=None, cvenHand2=None, cvenPerson=None,cvenPerson2=None,cvenPhone=None,cvenPhone2=None,factoryAddress=None,factoryGrade=None,
                 factorylocation=None,fregistFund=None,generalTaxpayer=None,inspectionResult=None,legalDepartmentsOpinion=None,legalRepresentative=None,mainServiceCustomerText=None,mainServiceCustomerType=None,monthlyDevelopment=None,
                 monthlyProduction=None, numberFactories=None,productCode=None,qualificationAuditResult=None,registeredCapital=None,startCooperationTime=None,vcCode=None,vcId=None,vcIdS=None,venAbbName=None,
                 vendorCode=None,vendorFiles=None,vendorName=None,venmoq=None,vensource=None,ventype=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        必填项参数
        cvenAddress：地址
        cvenHand：手机
        cvenPerson：联系人
        vcCode：供应商分类编码
        vcId：供应商分类ID
        venAbbName：供应商简称
        vendorCode：供应商编码
        vendorName：供应商名称
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResVendorAdd(object):
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

        # 2.根据传入的参数，进行数据正确性断言


class DataSwitchBanVendor(BaseData):
    """
    供应商启用禁用
    """
    def __init__(self, vendorId = None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        必填项参数
        vendorId  供应商ID
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResSwitchBanVendor(object):
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

        # 2.根据传入的参数，进行数据正确性断言


class ExportVendorAdd(BaseData):
    """
    供应商导出参数构建
    """
    def __init__(self, category=None, coreproduct=None, factoryGrade=None, factorylocation=None, pageNum=None,
                 pageSize=None, state=None, venAbbName=None, vendorCode=None, vensource=None, ventype=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        必填项参数
        category：	产品类目
        coreproduct：核心产品
        factoryGrade：工厂等级
        factorylocation：供应商使用定位
        pageNum：页码 默认为1
        pageSize：每页条数 默认15
        state：状态
        venAbbName：供应商简称
        vendorCode：供应商编码
        vensource：供应商来源
        ventype：供应商类型
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


class DataVendorInfo(BaseData):
    """
    查看供应商详情参数构建
    """
    def __init__(self, vendorId = None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        必填项参数
        vendorId：供应商ID
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class DataResVendorInfo(object):
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
        assert_that(data["obj"], has_key('venAbbName'))
        assert_that(data["obj"], has_key('vendorName'))
        assert_that(data["obj"], has_key('vendorId'))
        assert_that(data["obj"], has_key('vendorCode'))
        if "venAbbName" in data_req:
            assert_that(data["obj"]["venAbbName"], equal_to(data_req["venAbbName"]))
        if "vendorName" in data_req:
            assert_that(data["obj"]["vendorName"], equal_to(data_req["vendorName"]))
        if "vendorCode" in data_req:
            assert_that(data["obj"]["vendorCode"], equal_to(data_req["vendorCode"]))
        if "vendorId" in data_req:
            assert_that(data["obj"]["vendorId"], equal_to(data_req["vendorId"]))


class DataResVendorInfo1(object):
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

class UpdateVendorDate(BaseData):
    """
    供应商新增参数构建
    """
    def __init__(self, vendorId=None, accname=None, annualOutput=None, category=None, companyRegistrationTime=None, cooperativeAttribute=None,
                 cooperativePositioningcol=None, cooperativeStatus=None, coreproduct=None, cvenAccount=None, cvenAddress=None, cvenAddress2=None,
                 cvenBank=None, cvenHand=None, cvenHand2=None, cvenPerson=None,cvenPerson2=None,cvenPhone=None,cvenPhone2=None,factoryAddress=None,factoryGrade=None,
                 factorylocation=None,fregistFund=None,generalTaxpayer=None,inspectionResult=None,legalDepartmentsOpinion=None,legalRepresentative=None,mainServiceCustomerText=None,mainServiceCustomerType=None,monthlyDevelopment=None,
                 monthlyProduction=None, numberFactories=None,productCode=None,qualificationAuditResult=None,registeredCapital=None,startCooperationTime=None,vcCode=None,vcId=None,vcIdS=None,venAbbName=None,
                 vendorCode=None,vendorFiles=None,vendorName=None,venmoq=None,vensource=None,ventype=None):
        """
        初始化，设置各项数据
        设置时，使用显示参数传递；若为非必填参数，可以不传
        必填项参数
        cvenAddress：地址
        cvenHand：手机
        cvenPerson：联系人
        vcCode：供应商分类编码
        vcId：供应商分类ID
        venAbbName：供应商简称
        vendorCode：供应商编码
        vendorName：供应商名称
        """
        BaseData.__init__(self)
        self.params = unity.copy_dict(locals())

    def get(self):
        return self.params


# ------------- 响应值：BaseResData -------------- #
class UpdateResVendorDate(object):
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

        # 2.根据传入的参数，进行数据正确性断言
