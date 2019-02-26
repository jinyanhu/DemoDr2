from cof.conf import MyCfg     # 引用cof中的配置方法


class BaseHessian(object):
    def __init__(self):
        # 读取的配置文件的名称
        my_cfg = MyCfg('wwwarehouse.ini')
        # 配置段的名称
        my_cfg.set_section('wwwarehouse_api')
        # 根据key读value
        self.host = my_cfg.get('host')
        self.port = my_cfg.get('port')
        self.base_url = "http://" + self.host + ":" + self.port + "/"

if __name__ == "__main__":
    base_hessian = BaseHessian()
    print(base_hessian.host)
    print(base_hessian.port)