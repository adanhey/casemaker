from flask_public.flask_public import *
from SQLconnect.db_file import *
from models_update import *
from table_index import table_index
from xmind_maker import XmindMaker


@app.route('/createPublicCase', methods=['POST'])
@permission
@requires
def create_public_case():
    project_id = request.json['project_id']
    name = request.json['name']
    if not Project.query.filter(Project.id == project_id).first():
        return {"message": f"项目id：{project_id}不存在"}, 404
    elif PublicCase.query.filter(PublicCase.name == name, PublicCase.project_id == project_id).first():
        return {"message": f"项目下名称{name}已存在"}, 400
    commit1 = PublicCase(name=name, project_id=project_id, jsonData=request.json['jsonData'])
    db.session.add(commit1)
    db.session.commit()
    return {"message": "新增成功"}


@app.route('/updatePublicCase', methods=['POST'])
@requires
@permission
def update_public_case():
    case_id = request.json['id']
    project_id = request.json['project_id']
    name = request.json['name']
    if not Project.query.filter(Project.id == project_id).first():
        return {"message": f"项目id：{project_id}不存在"}, 404
    elif not PublicCase.query.filter(PublicCase.id == case_id).first():
        return {"message": f"公共用例id：{project_id}不存在"}, 404
    elif PublicCase.query.filter(PublicCase.name == name, PublicCase.project_id == project_id,
                                 PublicCase.id != case_id):
        return {"message": f"项目下名称{name}已存在"}, 400
    commit1 = PublicCase.query.filter(PublicCase.id == case_id).first()
    commit1.name, commit1.project_id, commit1.jsonData = name, project_id, request.json['jsonData']
    db.session.commit()
    return {"message": "修改成功"}


@app.route('/deletePublicCase', methods=['DELETE'])
@permission
def delete_model():
    case_id = request.form.get('id')
    if not PublicCase.query.filter(PublicCase.id == case_id).first():
        return {"message": f"项目id：{case_id}不存在"}, 404
    case1 = ModelPart.query.filter(ModelPart.id == case_id).first()
    db.session.delete(case1)
    db.session.commit()
    return "删除成功"


if __name__ == "__main__":
    app.run(host='10.53.3.46')
