from functools import wraps
from flask_public.sign_compare import sign_compare
from http import HTTPStatus
from flask import Flask, request
from flask_public.interface_require_index import *
from flask_public.interface_select_index import *
from flask_public.interface_full_data import *
from SQLconnect.db_file import *
from flask_public.interface_table_index import *

app = Flask(__name__)
ACCOUNTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")


def requires(func):
    @wraps(func)
    def inner():
        require_data = interfaceRequire[request.path]
        interface_info = request.json
        for require in require_data:
            if require not in interface_info:
                return {"message": f"请求体缺失{require}"}, 400
        return func()

    return inner


def permission(func):
    @wraps(func)
    def inner():
        if 'Authorization' not in request.headers:
            return {"message": "headers缺少Authorization", "status_code": 401}, 401
        auth = request.headers['Authorization']
        if not sign_compare(auth):
            return {"message": "签名校验失败", "status_code": HTTPStatus.FORBIDDEN}, 403
        return func()

    return inner


def create_commit(func):
    @wraps(func)
    def inner():
        full_data = interfaceFullData[request.path]
        table_index = interfaceTableIndex[request.path]
        interface_info = request.json
        if eval(f"{table_index}.query.filter({table_index}.name == interface_info['name']).first()"):
            return {"message": f"名称{interface_info['name']}已存在"}, 400
        add_string = ""
        for data in full_data:
            if data in interface_info:
                exec(f"{data} = interface_info['{data}']")
            else:
                exec(f"{data} = ''")
            add_string += f"{data}={data}"
        commit1 = eval(
            f"{table_index}({add_string})")
        db.session.add(commit1)
        db.session.commit()
        return func()

    return inner


def update_commit(func):
    @wraps(func)
    def inner():
        full_data = interfaceFullData[request.path]
        table_index = interfaceTableIndex[request.path]
        interface_info = request.json
        if eval(f"{table_index}.query.filter({table_index}.name == interface_info['name'],"
                f" {table_index}.id != interface_info['id']).first()"):
            return {"message": f"{interface_info['name']}已存在"}, 400
        elif not eval(f"{table_index}.query.filter({table_index}.id == interface_info['id']).first()"):
            return {"message": f"id不存在"}, 404
        else:
            pro1 = eval(f"{table_index}.query.filter({table_index}.id == interface_info['id']).first()")
            for data in full_data:
                if data in interface_info:
                    exec(f"pro1.{data} = interface_info['{data}']")
        db.session.commit()
        return func()

    return inner


def delete_check(func):
    @wraps(func)
    def inner():
        table_index = interfaceTableIndex[request.path]
        del_id = request.args.get("id")
        if not del_id:
            return {"message": "请求params缺少id"}, 400
        elif not eval(f"{table_index}.query.filter({table_index}.id == del_id).first()"):
            return {"message": "资源不存在"}, 404
        else:
            project1 = eval(f"{table_index}.query.filter({table_index}.id == del_id).first()")
            db.session.delete(project1)
            db.session.commit()
        return func()

    return inner


# def list_select(request_path):
#     table_index = interfaceTableIndex[request.path]
#     select_index = interface_select[request.path]
#     select_str = ""
#     for pam in select_index :
#         exec(f"{pam} = request.args.get('{pam}')")
#         if eval(f"{pam}"):
#             select_str += f"Project.{pam} == {pam}"
#     result = eval(f"Project.query.filter({select_str}).all()")
#     res = []


@app.errorhandler(403)
def handle_403_error(err):
    return {"message": "签名校验失败", "status_code": HTTPStatus.FORBIDDEN}
