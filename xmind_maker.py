import xmind
from dict_dir.translate_index import translate_dict


class XmindMaker:
    def __init__(self, filename, path, title=None, public_dic=None):
        self.workbook = xmind.load(filename)
        self.sheet = self.workbook.getPrimarySheet()
        self.path = path
        self.public_dic = public_dic
        if title:
            self.sheet.setTitle(title)

    def add_topic(self, parent_topic, title=None, note=None):
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
        if note:
            topic.setPlainNotes(note)
        if self.public_dic:
            for key, value in self.public_dic.items():
                if key == title:
                    for s in value:
                        self.add_topic(topic, s)
        return topic

    def set_note(self, topic, note):
        topic.setPlainNotes(note)

    def xmind_save(self):
        xmind.save(self.workbook, path=self.path)
