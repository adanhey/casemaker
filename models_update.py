import os
from models import *


def modify_model(name, key=None, value=None):
    dic = []
    for k, v in models.items():
        if name in k:
            dic.append(k)
    if len(dic) == 0:
        print("无匹配项")
    elif len(dic) == 1:
        if key in models[dic[0]]:
            models[dic[0]][key] = value
            with open("models.py", 'w+') as fi:
                fi.write('models = %s' % str(models))
                fi.close()
            print("修改成功")
        else:
            print("修改项不存在")
    else:
        re_string = "匹配数超过一："
        for st in dic:
            re_string += '%s, ' % st
        print(re_string)


def replace_model(name, dic):
    res = {}
    res[name] = dic
    # models[name] = dic
    with open("./models_copy.py", 'w+', encoding='utf-8') as f:
        # f.write(str(models))
        f.write(str(res))
        f.close()


# replace_model("1c11c", "{}")
# modify_model("工单流程", "type", ["1", "2", "3"])
