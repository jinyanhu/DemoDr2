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
class DataLogin(BaseData):
    """
    登录参数构建
    """
    def __init__(self, userName=None, password=None, dataType=None, code=None):
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
class DataResLogin(object):
    """
    s3账户数据
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
        assert_that(data["obj"], has_key('uid'))
        assert_that(data["obj"], has_key('token'))
        assert_that(data["obj"], has_key('realName'))
        assert_that(data["obj"], has_key('userId'))

        # 2.根据传入的参数，进行数据正确性断言
        assert_that(data["obj"]["qyType"], equal_to(data_req["dataType"]))

