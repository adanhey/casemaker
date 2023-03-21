from flask_public.flask_public import *
from SQLconnect.db_file import *

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
def delete_public_case():
    case_id = request.args.get('id')
    if not PublicCase.query.filter(PublicCase.id == case_id).first():
        return {"message": f"项目id：{case_id}不存在"}, 404
    case1 = PublicCase.query.filter(PublicCase.id == case_id).first()
    db.session.delete(case1)
    db.session.commit()
    return {"message": "删除成功"}


@app.route('/listPublicCase', methods=['GET'])
@permission
def get_public_case():
    select_pam = ['name']
    select_str = ""
    for pam in select_pam:
        exec(f"{pam} = request.args.get('{pam}')")
        if eval(f"{pam}"):
            select_str += f"PublicCase.{pam} == {pam}"
    result = eval(f"PublicCase.query.filter({select_str}).all()")
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


if __name__ == "__main__":
    app.run(host='10.53.3.46')
