

from hamcrest import *
import data_structure.unity as unity
from data_structure.chenfan.base import BaseData


class DataRouteEsb(BaseData):
    """
    征信进件esb加密
    """
    def __init__(self):
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


class DataResEsb(object):
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
        assert_that(data, has_key('msg'))





