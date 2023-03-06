from dict_dir.models import *
from dict_dir.public_case import *
from xmind_maker import *
import datetime

now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


class CaseType(XmindMaker):
    def __init__(self, requirement_name, filename, path, dic, name=None):
        super().__init__(filename, path)
        self.name = name
        self.dic = dic
        self.root_topic = self.add_topic("root", requirement_name)
        self.index_dict = self.dic[self.name]
        self.quote = self.index_dict['quote']
        self.quoted = self.index_dict['quoted']

    def quote_maker(self):
        quote_topic = self.add_topic(self.root_topic, "quote")
        self.round_maker(quote_topic, self.quote)

    def quoted_maker(self):
        quoted_topic = self.add_topic(self.root_topic, "quoted")
        for key, value in self.quoted.items():
            child_topic = self.add_topic(quoted_topic, key)
            special_topic = self.add_topic(child_topic, 'important_check')
            for i in value:
                self.add_topic(special_topic, i)
            dic = self.dic[key]
            self.round_maker(child_topic, dic)

    def special_maker(self, name, parent_topic):
        add_dict = models[name]
        special_topic = self.add_topic(parent_topic, "module_special_check")
        if "special" in add_dict:
            for special in add_dict['special']:
                self.add_topic(special_topic, special)

    def own_maker(self, name, topic):
        self.round_maker(topic, self.dic[name]['type'])

    def public_maker(self, public_list, topic):
        for public in public_list:
            self.add_topic(topic, public)

    def round_maker(self, topic, dic, public=1):
        for k, v in dic.items():
            child_topic = self.add_topic(topic, k)
            if public != 0:
                if k in public_case.keys():
                    public_topic = self.add_topic(child_topic, "public_case")
                    for public in public_case[k]:
                        self.add_topic(public_topic, public)
            if isinstance(v, dict):
                self.round_maker(child_topic, v)
            elif isinstance(v, list):
                child_topic.setPlainNotes('list')
                for i in v:
                    self.add_topic(child_topic, i)

    def make_case(self, is_quote=1, is_quoted=1, own=1):
        if is_quoted == 1:
            self.quoted_maker()
        if is_quote == 1:
            self.quote_maker()
        if own == 1:
            self.own_maker(self.name, self.root_topic)
        self.special_maker(self.name, self.root_topic)
        self.xmind_save()
        print("保存成功")


cases = CaseType("改动点", "%stest.xmind" % now, "./xmind_files/%stest.xmind" % now, models, "工单配置-流程节点")
cases.make_case()

# cases = CaseType("公共用例", "公共用例.xmind", "公共用例.xmind", public_case)
# cases.round_maker(cases.root_topic, cases.dic, 0)
# cases.xmind_save()
