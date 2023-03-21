import os
from flask_public.flask_public import *
from SQLconnect.db_file import *
from models_update import *
from SQLconnect.table_index import table_index
from xmind_maker import XmindMaker


@app.route('/importModel', methods=['POST'])
@permission
def import_model():
    name = request.form.get('name')
    pro_id = request.form.get('pro_id')
    if not Project.query.filter(Project.id == pro_id).first():
        return {"message": f"项目id：{pro_id}不存在"}, 404
    elif ModelPart.query.filter(ModelPart.name == name, ModelPart.project_id == pro_id).first():
        return {"message": f"项目下名称{name}已存在"}, 400
    xmind_file = request.files.get("file")
    content = xmindparser.xmind_to_dict(xmind_file)
    real_content = content[0]['topic']
    sub_dic = sub_topic_title(real_content)
    commit1 = ModelPart(name=name, project_id=pro_id, quote=sub_dic['quote'], quoted=sub_dic['quoted'],
                        module_special_check=sub_dic['module_special_check'])
    db.session.add(commit1)
    db.session.commit()
    model_id = ModelPart.query.filter(ModelPart.name == name).first().id
    message = save_cases(sub_dic['type'], model_id)
    return {"message": message}


@app.route('/getExampleFile', methods=['GET'])
def get_example_file():
    f = open("./title.xmind", 'rb')
    re_file = f
    return re_file


@app.route('/updateModel', methods=['POST'])
@permission
def update_model():
    model_id = request.form.get('id')
    name = request.form.get('name')
    pro_id = request.form.get('pro_id')
    if not Project.query.filter(Project.id == pro_id).first():
        return {"message": f"项目id：{pro_id}不存在"}, 404
    elif ModelPart.query.filter(ModelPart.name == name, ModelPart.project_id == pro_id,
                                ModelPart.id != model_id).first():
        return {"message": f"项目下名称{name}已存在"}, 400
    xmind_file = request.files.get("file")
    content = xmindparser.xmind_to_dict(xmind_file)
    real_content = content[0]['topic']
    sub_dic = sub_topic_title(real_content)
    commit1 = ModelPart.query.filter(ModelPart.id == model_id).first()
    commit1.quote, commit1.quoted, commit1.name, commit1.module_special_check = sub_dic['quote'], sub_dic[
        'quoted'], name, \
        sub_dic['module_special_check']
    db.session.commit()
    message = save_cases(sub_dic['type'], model_id, update=1)
    return {"message": message}


@app.route('/getModelXmind', methods=['GET'])
@permission
def get_model_xmind():
    sub_dic = {"type": {}}
    model_id = request.args.get('id')
    if not model_id:
        return {"message": f"params缺失id"}, 400
    elif not ModelPart.query.filter(ModelPart.id == model_id).first():
        return {"message": f"模块id：{model_id}不存在"}, 404
    sub_dic['quote'] = ModelPart.query.filter(ModelPart.id == model_id).first().quote
    sub_dic['quoted'] = ModelPart.query.filter(ModelPart.id == model_id).first().quoted
    sub_dic['module_special_check'] = ModelPart.query.filter(ModelPart.id == model_id).first().module_special_check
    name = ModelPart.query.filter(ModelPart.id == model_id).first().name
    for key, value in table_index.items():
        result = eval(f"{value}.query.filter({value}.modelPartId == model_id).first()")
        if result:
            sub_dic['type'][key] = result.jsonData
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    maker = XmindMaker("%stest.xmind" % now, "./%stest.xmind" % now, name)
    maker.add_topic('root', name)
    make_xmind(maker, sub_dic, maker.sheet.getRootTopic())
    maker.xmind_save()
    f = open(maker.path, 'rb')
    re_file = f
    return re_file


@app.route('/importPublicCase', methods=['GET'])
@permission
def import_public_case():
    sub_dic = {}
    result = PublicCase.query.filter().all()
    for i in result:
        sub_dic[i.name] = i.jsonData
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    maker = XmindMaker("%stest.xmind" % now, "./%stest.xmind" % now)
    maker.add_topic('root', "公共用例")
    make_xmind(maker, sub_dic, maker.sheet.getRootTopic())
    maker.xmind_save()
    f = open(maker.path, 'rb')
    re_file = f
    return re_file


@app.route('/deleteModel', methods=['DELETE'])
@permission
def delete_model():
    model_id = request.form.get('id')
    if not ModelPart.query.filter(ModelPart.id == model_id).first():
        return {"message": f"项目id：{model_id}不存在"}, 404
    for key, value in table_index.items():
        result = eval(f"{value}.query.filter({value}.modelPartId == model_id).first()")
        if result:
            db.session.delete(result)
            db.session.commit()
    model1 = ModelPart.query.filter(ModelPart.id == model_id).first()
    db.session.delete(model1)
    db.session.commit()
    return "删除成功"


@app.route('/listModel', methods=['GET'])
@permission
def list_model():
    select_pam = ['name']
    select_str = ""
    for pam in select_pam:
        exec(f"{pam} = request.args.get('{pam}')")
        if eval(f"{pam}"):
            select_str += f"ModelPart.{pam} == {pam}"
    result = eval(f"ModelPart.query.filter({select_str}).all()")
    res = []
    for i in result:
        mid_dic = {}
        for key, value in i.__dict__.items():
            if key == '_sa_instance_state':
                pass
            elif isinstance(value, datetime):
                mid_dic[key] = str(value)
            else:
                mid_dic[key] = value
        res.append(mid_dic)
    return {"查询结果": res}


def make_xmind(maker, dic, topic):
    if isinstance(dic, dict):
        for key, value in dic.items():
            child_topic = maker.add_topic(topic, key)
            if isinstance(value, dict) or isinstance(value, list):
                make_xmind(maker, value, child_topic)
    elif isinstance(dic, list):
        for obj in dic:
            if isinstance(obj, dict) or isinstance(obj, list):
                make_xmind(maker, obj, topic)
            else:
                maker.add_topic(topic, obj)


def save_cases(content_dic, model_id, update=None):
    if update:
        for key, value in content_dic.items():
            if key in table_index:
                comer = eval(f"{table_index[key]}.query.filter({table_index[key]}.modelPartId == model_id).first()")
                comer.jsonData = value
        db.session.commit()
        return "修改成功"
    for key, value in content_dic.items():
        if key in table_index:
            commit = eval(f"{table_index[key]}(modelPartId=model_id, jsonData=value)")
            db.session.add(commit)
    db.session.commit()
    return "新增成功"


def sub_topic_title(content, dic=None):
    if dic is None:
        dic = {}
    for i in content['topics']:
        for key, value in translate_dict.items():
            if value == i['title']:
                i['title'] = key
        dic[i['title']] = {}
        if "topics" in i:
            sub_topic_title(i, dic[i['title']])
    return dic


if __name__ == "__main__":
    app.run(host='10.53.3.46')
