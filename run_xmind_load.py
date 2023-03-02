import xmindparser
from models_update import replace_model
from xmind_maker import sub_topic_title

final_dict = {}
content = xmindparser.xmind_to_dict('title.xmind')
dd = sub_topic_title(content[0]['topic'], final_dict)
replace_model('替换模块名称', dd)
