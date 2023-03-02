import xmind
import xmindparser
from translate_index import translate_dict


class XmindMaker:
    def __init__(self, filename, path, title=None):
        self.workbook = xmind.load(filename)
        self.sheet = self.workbook.getPrimarySheet()
        self.path = path
        if title:
            self.sheet.setTitle(title)

    def add_topic(self, parent_topic, title=None):
        if parent_topic == "root":
            topic = self.sheet.getRootTopic()
        else:
            topic = parent_topic.addSubTopic()
        if title:
            for k, v in translate_dict.items():
                if title == k:
                    title = v
                    break
            topic.setTitle(title)
        return topic

    def set_note(self, topic, note):
        topic.setPlainNotes(note)

    def xmind_save(self):
        xmind.save(self.workbook, path=self.path)


def sub_topic_title(cont, dic):
    for i in cont['topics']:
        if i['title'] in ['special', 'asd']:
            dic[i['title']] = []
            if "topics" in i:
                for j in i['topics']:
                    dic[i['title']].append(j['title'])
        else:
            dic[i['title']] = {}
            if "topics" in i:
                sub_topic_title(i, dic[i['title']])
    return dic

# a = XmindMaker('test.xmind', 'test.xmind')
# t1 = a.add_topic(parent_topic='root')
# a.add_topic(parent_topic=t1, title='测试节点2')
# a.xmind_save()
# final_dict = {}
# content = xmindparser.xmind_to_dict('title.xmind')
# print(content)
# print(sub_topic_title(content[0]['topic'], final_dict))
