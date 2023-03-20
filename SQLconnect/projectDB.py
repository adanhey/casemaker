from flask_public.flask_public import *
from SQLconnect.db_file import *


@app.route('/createProject', methods=['POST'])
@permission
@requires
@create_commit
def create_project():
    return {"message": "添加成功"}


@app.route('/updateProject', methods=['POST'])
@permission
@requires
@update_commit
def update_project():
    return {"message": "修改成功"}


@app.route('/deleteProject', methods=['DELETE'])
@permission
@delete_check
def delete_project():
    return {"message": "删除成功"}


@app.route('/listProject', methods=['GET'])
@permission
def list_project():
    select_pam = ['name']
    select_str = ""
    for pam in select_pam:
        exec(f"{pam} = request.args.get('{pam}')")
        if eval(f"{pam}"):
            select_str += f"Project.{pam} == {pam}"
    result = eval(f"Project.query.filter({select_str}).all()")
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
