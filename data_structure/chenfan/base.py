from hamcrest import *


class BaseData(object):
    """
    数据的基础类
    """
    def __init__(self):
        """
        将初始化传入的参数赋值给成员变量
        """
        self.params = dict()

    def get(self):
        """
        返回初始的数据
        """
        return self.params

