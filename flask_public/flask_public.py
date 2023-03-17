from functools import wraps
from flask_public.sign_compare import sign_compare
from http import HTTPStatus
from flask import Flask, request
from flask_public.interface_require_index import *
from flask_public.interface_full_data import *
from SQLconnect.db_file import *
from flask_public.interface_table_index import *

app = Flask(__name__)
ACCOUNTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")


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


def require_check(func):
    @wraps(func)
    def inner():
        require_data = interfaceRequire[request.path]
        table_index = interfaceTableIndex[require_data]
        interface_info = request.json
        for require in require_data:
            if require not in interface_info:
                return {"message": f"请求体缺失{require}"}, 400
            elif eval(f"{table_index}.query.filter({table_index}.name == interface_info['name']).first()"):
                return {"message": f"名称{interface_info['name']}已存在"}, 400
        return func()

    return inner()


def create_data_commit(func):
    @wraps(func)
    def inner():
        full_data = interfaceFullData[request.path]
        table_index = interfaceTableIndex[request.path]
        interface_info = request.json
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

    return inner()


@app.errorhandler(403)
def handle_403_error(err):
    return {"message": "签名校验失败", "status_code": HTTPStatus.FORBIDDEN}
