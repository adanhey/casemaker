import xmind


class XmindMaker:
    def __init__(self, filename, path, title=None):
        self.workbook = xmind.load(filename)
        self.sheet = self.workbook.getPrimarySheet()
        self.path = path
        if title:
            self.sheet.setTitle(title)

    def add_topic(self, parent_topic, title=""):
        if parent_topic == "root":
            topic = self.sheet.getRootTopic()
        else:
            topic = parent_topic.addSubTopic()
        topic.setTitle(title)
        return topic

    def set_note(self, topic, note):
        topic.setPlainNotes(note)

    def xmind_save(self):
        xmind.save(self.workbook, path=self.path)


# a = XmindMaker('test.xmind', 'test.xmind')
# t1 = a.add_topic(parent_topic='root', title='测试')
# a.add_topic(parent_topic=t1, title='测试节点2')
# a.xmind_save()
