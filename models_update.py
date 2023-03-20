from dict_dir.models import *
from dict_dir.translate_index import *
import xmindparser


class XmindLeap:
    def __init__(self, dic, **kwargs):
        self.dic = dic
        self.path_dict = kwargs

    def modify_model(self, replace_dic, replace_key=None, replace_value=None):
        for key, value in replace_dic.items():
            if key == replace_key:
                replace_dic[key] = replace_value
            elif isinstance(value, dict):
                self.modify_model(value, replace_key, replace_value)

    def sub_topic_title(self, content, dic=None):
        if dic is None:
            dic = {}
        for i in content['topics']:
            if 'note' in i:
                if 'list' in i['note']:
                    for key, value in translate_dict.items():
                        if value == i['title']:
                            i['title'] = key
                    dic[i['title']] = []
                    if "topics" in i:
                        for j in i['topics']:
                            for k, v in translate_dict.items():
                                if v == j['title']:
                                    j['title'] = k
                            dic[i['title']].append(j['title'])
            else:
                for k, v in translate_dict.items():
                    if v == i['title']:
                        i['title'] = k
                dic[i['title']] = {}
                if "topics" in i:
                    self.sub_topic_title(i, dic[i['title']])
        return dic

    def replace_model(self, path):
        with open(path, 'w+', encoding='utf-8') as f:
            f.write("models = %s" % str(self.dic).replace("'", '"'))

    def case_leap(self, save_path='./dict_dir/models_copy.py'):
        for key, path in self.path_dict.items():
            content = xmindparser.xmind_to_dict(path)
            real_content = content[0]['topic']
            dic = self.sub_topic_title(real_content)
            self.dic[key] = dic
        with open(save_path, 'w+', encoding='utf-8') as f:
            f.write("models = %s" % str(self.dic).replace("'", '"'))

    def interface_content(self, file):
        content = xmindparser.xmind_to_dict(file)
        # real_content = content[0]['topic']
        return content

# a = XmindLeap(models, 备件出库="xmind_files/save_dir/备件出库.xmind", 仓库管理="xmind_files/save_dir/仓库管理.xmind",
#               备件类型管理="xmind_files/save_dir/备件类型管理.xmind", 备件管理="xmind_files/save_dir/备件管理.xmind",
#               备件入库="xmind_files/save_dir/备件入库.xmind", 备件配置="xmind_files/save_dir/备件配置.xmind",
#               个人备件操作="xmind_files/save_dir/个人备件操作.xmind",
#               个人备件清单="xmind_files/save_dir/个人备件清单.xmind",
#               个人使用记录="xmind_files/save_dir/个人使用记录.xmind",
#               工单超时配置="xmind_files/save_dir/工单超时配置.xmind",
#               工单池工单="xmind_files/save_dir/工单池工单.xmind", 工单池管理="xmind_files/save_dir/工单池管理.xmind",
#               工单池员工管理="xmind_files/save_dir/工单池员工管理.xmind",
#               工单节点配置="xmind_files/save_dir/工单节点配置.xmind",
#               工单类型管理="xmind_files/save_dir/工单类型管理.xmind",
#               工单流转规则="xmind_files/save_dir/工单流转规则.xmind",
#               工单预警配置="xmind_files/save_dir/工单预警配置.xmind",
#               供应商管理="xmind_files/save_dir/供应商管理.xmind",
#               回访配置="xmind_files/save_dir/回访配置.xmind",库位管理及库存="xmind_files/save_dir/库位管理及库存.xmind")
# a.case_leap()
