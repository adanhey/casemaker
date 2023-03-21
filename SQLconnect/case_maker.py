from flask_public.flask_public import *
from SQLconnect.db_file import *
from SQLconnect.modelsDB import *


@app.route('/exportModelCase', methods=['POST'])
@permission
def export_model_case():
    sub_dic = {"type": {}}
    public_dict = {}
    public_case = PublicCase.query.filter().all()
    for i in public_case:
        public_dict[i.name] = i.jsonData
    project_id = request.json['project_id']
    model_name = request.json['model_name']
    model_info = ModelPart.query.filter(ModelPart.name == model_name, ModelPart.project_id == project_id).first()
    for key, value in table_index.items():
        result = eval(f"{value}.query.filter({value}.modelPartId == model_info.id).first()")
        if result:
            sub_dic['type'][key] = result.jsonData
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    maker = XmindMaker("%stest.xmind" % now, "./%stest.xmind" % now, public_dic=public_dict)
    maker.add_topic('root', model_name)
    make_xmind(maker, sub_dic['type'], maker.sheet.getRootTopic())
    quote_maker(maker, model_info.quote)
    quoted_maker(maker, model_info.quoted)
    maker.xmind_save()
    f = open(maker.path, 'rb')
    re_file = f
    return re_file


def quote_maker(maker, quote_dic):
    main_topic = maker.sheet.getRootTopic()
    quote_topic = maker.add_topic(main_topic, "quote")
    for key, value in quote_dic.items():
        children = maker.add_topic(quote_topic, key)
        make_xmind(maker, value, children)
        be_q = maker.add_topic(children, "引用关注点")
        if ModelPart.query.filter(ModelPart.name == key).first():
            be_quote = ModelPart.query.filter(ModelPart.name == key).first().be_quote
            make_xmind(maker, be_quote, be_q)


def quoted_maker(maker, quoted_dic):
    main_topic = maker.sheet.getRootTopic()
    quoted_topic = maker.add_topic(main_topic, "quoted")
    for key, value in quoted_dic.items():
        children = maker.add_topic(quoted_topic, key)
        make_xmind(maker, value, children)
        quoted_model = ModelPart.query.filter(ModelPart.name == key).first()
        if quoted_model:
            sub_dic = {"type": {}}
            for k, v in table_index.items():
                result = eval(f"{v}.query.filter({v}.modelPartId == quoted_model.id).first()")
                if result:
                    sub_dic['type'][k] = result.jsonData
            make_xmind(maker, sub_dic['type'], children)


if __name__ == "__main__":
    app.run(host='10.53.3.46')
