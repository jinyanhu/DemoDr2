

"""
该模块封装属于当前服务的http基本操作
"""

from utils.conf import MyCfg     # 引用cof中的配置方法


class BaseHttp(object):
    def __init__(self):
        # 1.设置默认的header，内容遵循restful接口规范要求
        self.header = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            # "user_ip": "101.69.247.106",
            # "user_agent": "pc"
        }

        # 2.读取配置
        # 读取的配置文件的名称
        my_cfg = MyCfg('chenfan.ini')
        # 配置段的名称
        my_cfg.set_section('esb_api')
        # 根据key读value
        self.host = my_cfg.get('host')
        self.port = my_cfg.get('port')
        self.url = "http://" + self.host + ":" + self.port



if __name__ == "__main__":
    base_http = BaseHttp()

