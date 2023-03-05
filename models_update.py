from dict_dir.models import *
from dict_dir.translate_index import *
import xmindparser


class XmindLeap:
    def __init__(self, path, dic):
        self.path = path
        self.dic = dic
        self.content = xmindparser.xmind_to_dict(self.path)
        self.real_content = self.content[0]['topic']

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

    def replace_model(self, name, dic, path):
        self.dic[name] = dic
        with open(path, 'w+', encoding='utf-8') as f:
            f.write(str(models))

    def case_leap(self, name, path='./dict_dir/models_copy.py'):
        dic = self.sub_topic_title(self.real_content)
        self.replace_model(name, dic, path)


a = XmindLeap("xmind_files/title.xmind", models)
a.case_leap("xixixixixi")
