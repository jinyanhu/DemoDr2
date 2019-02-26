# coding=utf-8

"""
获取配置文件中的测试集
using method:
    input command in cmd linke "python runners.py case_2 case_1"
"""

import os
import sys
import json
import importlib
from nose import suite
from nose import loader
from pprint import pprint
from optparse import OptionParser

import cof.file as CoFileM
import cof.conf as CoConfM

# 调试开关
IS_DEBUG = False

# 获取工程路径
app_loc = CoFileM.get_app_loc()
app_cfg = CoConfM.get_cfg_type()
app_gbl_cfg_file = CoConfM.get_cfg_type_path()

# 在指定的配置文件（默认为“suites.json”）中，读指定的测试集
# 配置文件路径为：config目录--环境类型--配置文件名
opt_parser = OptionParser()
opt_parser.add_option("-s", "--suite", dest="suite", help=u"指定运行的测试套件", metavar="SUITE")
(options, opt_args) = opt_parser.parse_args()
suite_opt = options.suite

if not suite_opt:
    suite_config = app_loc + "config" + os.sep + app_cfg + os.sep + "suites.json"
else:
    # 到指定的目录获取对应的测试集配置
    suite_config = app_loc + "config" + os.sep + app_cfg + os.sep + suite_opt + ".json"


def set_case_list():
    """
    从命令行读取需要运行的测试集，返回测试集列表
    """
    argvs = sys.argv
    if len(argvs) <= 1:         # 没有指定测试用例集，默认运行所有测试用例（nose自动识别）
        print("no specified cases, could run all cases")
        return None

    if argvs[1] == "--all":     # 运行配置文件中的所有用例集（待实现）
        print("run all cases specified in json file")
        return None

    # 读suites.json配置文件，获取所有划分的测试集
    cof_file = open(suite_config)
    case_set = json.load(cof_file)

    # 测试集
    suite_list = list()
    for i in range(1, len(argvs)):
        case_set_name = argvs[i]
        if case_set_name not in case_set.keys():
            # 输入的用例集名称不存在于配置文件指定的测试集中
            print("case set name(s): \"%s\" is(are) not include in case set names in json file" % case_set_name)
            # raise NameError
            continue
        else:
            case_tmp = case_set[case_set_name]
            suite_list.append(case_tmp)

    if len(suite_list) == 0:
        print("测试集为空，停止运行")
        exit(0)

    return suite_list


def generate_suites(root, test_sets):
    """
    生成测试套件
    root 表示测试用例路径， test_sets 代表cases列表
    """
    suites = suite.LazySuite()

    sys.path.append(root)
    print(root)
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../testcases")
    if IS_DEBUG:
        pprint(sys.path)

    for ts_name in test_sets:
        for tc in test_sets[ts_name]:
            print("tc xxxxxxx: ", tc)
            tc_complete = ts_name + "." + tc    # 用例文件完整的路径
            print("tc_complete: ", tc_complete)
            module = importlib.import_module(tc_complete)  # 这里为什么要importlib？？？
            print("module: ", module)
            suites.addTest(loader.TestLoader().loadTestsFromModule(module))
    return suites


if __name__ == "__main__":
    pass
