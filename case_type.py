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
            print(self.index_dict)
            self.quote = self.index_dict['quote']
            self.quoted = self.index_dict['quoted']
            self.root_topic = self.add_topic("root", requirement_name)
        else:
            print("模块名称不存在")

    def quote_maker(self):
        quote_topic = self.add_topic(self.root_topic, "引用模块")
        for k, v in self.quote.items():
            if k in models.keys():
                search_dict = models[k]
                quote2_topic = self.add_topic(quote_topic, k)
                if "data" in v:
                    quote3_topic = self.add_topic(quote2_topic, "数据引用：验证所有可创建数据可用")
                    quote4_topic = self.add_topic(quote3_topic, "关键验证点")
                    for create_important in search_dict['interface']['create'].keys():
                        self.add_topic(quote4_topic, create_important)
                self.special_maker(k, quote2_topic)
            else:
                print("引用模块%s不存在" % k)

    def quoted_maker(self):
        quoted_topic = self.add_topic(self.root_topic, "被引用模块")
        for k, v in self.quoted.items():
            child_topic = self.add_topic(quoted_topic, k)
            self.own_maker(k, child_topic)

    def special_maker(self, name, parent_topic):
        add_dict = models[name]
        special_topic = self.add_topic(parent_topic, "模块特征测试点")
        for special in add_dict['special']:
            self.add_topic(special_topic, special)

    def own_maker(self, name, topic):
        if name in models.keys():
            dic = models[name]
            self.special_maker(name, topic)
            for tp, tv in dic['type'].items():
                if tp == "server_side_logic":
                    side_topic = self.add_topic(topic, "后端逻辑")
                    self.server_side_logic_maker(tv, side_topic)
                elif tp == "interface_setting":
                    side_topic = self.add_topic(topic, "接口配置")
                    self.interface_setting_maker(tv, side_topic)
                elif tp == "web_client":
                    side_topic = self.add_topic(topic, "web前端")
                    self.web_client_maker(tv, side_topic)
                elif tp == "client_serve":
                    side_topic = self.add_topic(topic, "后端-前端数据传输")
                    self.client_serve_maker(tv, side_topic)
                elif tp == "app_client":
                    side_topic = self.add_topic(topic, "app变更")
                    self.app_client_maker(tv, side_topic)
                elif tp == "iot_data_collect":
                    side_topic = self.add_topic(topic, "物联设备数据采集")
                    self.iot_data_collect_maker(tv, side_topic)
                elif tp == "iot_data_issue":
                    side_topic = self.add_topic(topic, "物联设备数据下发")
                    self.iot_data_issue_maker(tp, side_topic)
        else:
            print("%s不存在" % name)

    def public_maker(self, public_list, topic):
        for public in public_list:
            self.add_topic(topic, public)

    def server_side_logic_maker(self, dic, topic):
        if 'outside_server' in dic.keys():
            child_topic = self.add_topic(topic, "外部服务逻辑")
            public_topic = self.add_topic(child_topic, "公共用例")
            for outside_server in dic['outside_server']:
                self.add_topic(child_topic, outside_server)
            self.public_maker(public_case['server_side_logic']['outside_server'], public_topic)
        if 'script' in dic.keys():
            child_topic = self.add_topic(topic, "内部脚本")
            public_topic = self.add_topic(child_topic, "公共用例")
            for script in dic['script']:
                self.add_topic(child_topic, script)
            self.public_maker(public_case['server_side_logic']['script'], public_topic)
        if 'own_logic' in dic.keys():
            child_topic = self.add_topic(topic, "内部逻辑")
            public_topic = self.add_topic(child_topic, "公共用例")
            for own_logic in dic['own_logic']:
                self.add_topic(child_topic, own_logic)
            self.public_maker(public_case['server_side_logic']['own_logic'], public_topic)

    def interface_setting_maker(self, dic, topic):
        if 'create' in dic.keys():
            child_topic = self.add_topic(topic, "新增接口")
            public_topic = self.add_topic(child_topic, "公共用例")
            pass
        if 'update' in dic.keys():
            child_topic = self.add_topic(topic, "编辑接口")
            public_topic = self.add_topic(child_topic, "公共用例")
            pass
        if 'list' in dic.keys():
            child_topic = self.add_topic(topic, "查询接口")
            public_topic = self.add_topic(child_topic, "公共用例")
            pass
        if 'delete' in dic.keys():
            child_topic = self.add_topic(topic, "删除接口")
            public_topic = self.add_topic(child_topic, "公共用例")
            pass
        if 'exec' in dic.keys():
            child_topic = self.add_topic(topic, "执行接口")
            public_topic = self.add_topic(child_topic, "公共用例")
            pass

    def web_client_maker(self, dic, topic):
        pass

    def client_serve_maker(self, dic, topic):
        pass

    def app_client_maker(self, dic, topic):
        pass

    def iot_data_collect_maker(self, dic, topic):
        pass

    def iot_data_issue_maker(self, dic, topic):
        pass

    def make_case(self, is_quote=1, is_quoted=1, own=1):
        if is_quoted == 1:
            self.quoted_maker()
        if is_quote == 1:
            self.quote_maker()
        if own == 1:
            self.own_maker(self.name, self.root_topic)
        self.xmind_save()


bv = CaseType("改动点", "工单配置-流程节点", "%stest.xmind" % now, "%stest.xmind" % now)
bv.make_case()
