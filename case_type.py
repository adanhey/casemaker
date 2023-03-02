from models import *
from case_base import *
from xmind_maker import *
import datetime

now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


class CaseType(XmindMaker):
    def __init__(self, requirement_name, name, filename, path):
        super().__init__(filename, path)
        self.name = name
        if name in models.keys():
            self.index_dict = models[self.name]
            self.quote = self.index_dict['quote']
            self.quoted = self.index_dict['quoted']
            self.root_topic = self.add_topic("root", requirement_name)
        else:
            print("模块名称不存在")

    def quote_maker(self):
        quote_topic = self.add_topic(self.root_topic, "quote")
        for k, v in self.quote.items():
            if k in models.keys():
                search_dict = models[k]
                quote2_topic = self.add_topic(quote_topic, k)
                if "data" in v:
                    quote3_topic = self.add_topic(quote2_topic, "quote_data_check")
                    quote4_topic = self.add_topic(quote3_topic, "important_check")
                    for create_important in search_dict['interface']['create'].keys():
                        self.add_topic(quote4_topic, create_important)
                self.special_maker(k, quote2_topic)
            else:
                print("引用模块%s不存在" % k)

    def quoted_maker(self):
        quoted_topic = self.add_topic(self.root_topic, "quoted")
        for k, v in self.quoted.items():
            child_topic = self.add_topic(quoted_topic, k)
            special_topic = self.add_topic(child_topic, 'important_check')
            for j in v:
                self.add_topic(special_topic, j)
            self.own_maker(k, child_topic)

    def special_maker(self, name, parent_topic):
        add_dict = models[name]
        special_topic = self.add_topic(parent_topic, "module_special_check")
        for special in add_dict['special']:
            self.add_topic(special_topic, special)

    def own_maker(self, name, topic):
        if name in models.keys():
            dic = models[name]
            self.special_maker(name, topic)
            for tp, tv in dic['type'].items():
                if tp == "server_side_logic":
                    side_topic = self.add_topic(topic, "server_side_logic")
                    self.server_side_logic_maker(tv, side_topic)
                elif tp == "interface_setting":
                    side_topic = self.add_topic(topic, "interface_setting")
                    self.interface_setting_maker(tv, side_topic)
                elif tp == "web_client":
                    side_topic = self.add_topic(topic, "web_client")
                    self.web_client_maker(tv, side_topic)
                elif tp == "client_serve":
                    side_topic = self.add_topic(topic, "client_serve")
                    self.client_serve_maker(tv, side_topic)
                elif tp == "app_client":
                    side_topic = self.add_topic(topic, "app_client")
                    self.app_client_maker(tv, side_topic)
                elif tp == "iot_data_collect":
                    side_topic = self.add_topic(topic, "iot_data_collect")
                    self.iot_data_collect_maker(tv, side_topic)
                elif tp == "iot_data_issue":
                    side_topic = self.add_topic(topic, "iot_data_issue")
                    self.iot_data_issue_maker(tp, side_topic)
        else:
            print("%s不存在" % name)

    def public_maker(self, public_list, topic):
        for public in public_list:
            self.add_topic(topic, public)

    def server_side_logic_maker(self, dic, topic):
        if 'outside_server' in dic.keys():
            child_topic = self.add_topic(topic, "outside_server")
            public_topic = self.add_topic(child_topic, "public_case")
            for outside_server in dic['outside_server']:
                self.add_topic(child_topic, outside_server)
            self.public_maker(public_case['server_side_logic']['outside_server'], public_topic)
        if 'script' in dic.keys():
            child_topic = self.add_topic(topic, "script")
            public_topic = self.add_topic(child_topic, "public_case")
            for script in dic['script']:
                self.add_topic(child_topic, script)
            self.public_maker(public_case['server_side_logic']['script'], public_topic)
        if 'own_logic' in dic.keys():
            child_topic = self.add_topic(topic, "own_logic")
            public_topic = self.add_topic(child_topic, "public_case")
            for own_logic in dic['own_logic']:
                self.add_topic(child_topic, own_logic)
            self.public_maker(public_case['server_side_logic']['own_logic'], public_topic)

    def interface_setting_maker(self, dic, topic):
        for k, v in dic.items():
            child_topic = self.add_topic(topic, k)
            public_topic = self.add_topic(child_topic, "public_case")
            if v != {}:
                for z, x in v.items():
                    sec_child = self.add_topic(child_topic, z)
                    for i in x:
                        self.add_topic(sec_child, i)
            if k in public_case['interface_setting']:
                self.public_maker(public_case['interface_setting'][k], public_topic)

    def web_client_maker(self, dic, topic):
        if 'pages' in dic:
            for k, v in dic['pages'].items():
                child_topic = self.add_topic(topic, k)
                if v != {}:
                    for z, x in v.items():
                        sec_child = self.add_topic(child_topic, z)
                        public_topic = self.add_topic(sec_child, "public_case")
                        for i in x:
                            self.add_topic(sec_child, i)
                        if z in public_case['web_client']:
                            self.public_maker(public_case['web_client'][z], public_topic)

    def client_serve_maker(self, dic, topic):
        for k, v in dic.items():
            child_topic = self.add_topic(topic, k)
            public_topic = self.add_topic(child_topic, "public_case")
            if v != {}:
                for z, x in v.items():
                    sec_child = self.add_topic(child_topic, z)
                    for i in x:
                        self.add_topic(sec_child, i)
            if k in public_case['client_serve']:
                self.public_maker(public_case['client_serve'][k], public_topic)

    def app_client_maker(self, dic, topic):
        if 'pages' in dic:
            for k, v in dic['pages'].items():
                child_topic = self.add_topic(topic, k)
                if v != {}:
                    for z, x in v.items():
                        sec_child = self.add_topic(child_topic, z)
                        public_topic = self.add_topic(sec_child, "public_case")
                        for i in x:
                            self.add_topic(sec_child, i)
                        if z in public_case['app_client']:
                            self.public_maker(public_case['app_client'][z], public_topic)

    def iot_data_collect_maker(self, dic, topic):
        for k, v in dic.items():
            child_topic = self.add_topic(topic, k)
            public_topic = self.add_topic(child_topic, "public_case")
            if v != {}:
                for z, x in v.items():
                    sec_child = self.add_topic(child_topic, z)
                    for i in x:
                        self.add_topic(sec_child, i)
            if k in public_case['iot_data_collect']:
                self.public_maker(public_case['iot_data_collect'][k], public_topic)

    def iot_data_issue_maker(self, dic, topic):
        for k, v in dic.items():
            child_topic = self.add_topic(topic, k)
            public_topic = self.add_topic(child_topic, "public_case")
            if v != {}:
                for z, x in v.items():
                    sec_child = self.add_topic(child_topic, z)
                    for i in x:
                        self.add_topic(sec_child, i)
            if k in public_case['iot_data_issue']:
                self.public_maker(public_case['iot_data_issue'][k], public_topic)

    def make_case(self, is_quote=1, is_quoted=1, own=1):
        if is_quoted == 1:
            self.quoted_maker()
        if is_quote == 1:
            self.quote_maker()
        if own == 1:
            self.own_maker(self.name, self.root_topic)
        self.xmind_save()
        print("保存成功")


bv = CaseType("改动点", "工单配置-流程节点", "%stest.xmind" % now, "%stest.xmind" % now)
bv.make_case()
