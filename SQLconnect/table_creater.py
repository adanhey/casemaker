from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import SQLconnect.DBconfig  # 导入配置文件
from datetime import *

app = Flask(__name__)
app.config.from_object(SQLconnect.DBconfig)
db = SQLAlchemy(app)


# 创建表模型类对象
#
#


# class Project(db.Model):
#     __tablename__ = 'project'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(50), nullable=False)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class ModelPart(db.Model):
#     __tablename__ = 'modelPart'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     project_id = db.Column(db.Integer, nullable=False)
#     name = db.Column(db.String(50), nullable=False)
#     quote = db.Column(db.String(50), nullable=False)
#     quoted = db.Column(db.String(50), nullable=False)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class ServerSideData(db.Model):
#     __tablename__ = 'serverSide'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     modelPartId = db.Column(db.Integer, nullable=False)
#     jsonData = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class InterfaceSetting(db.Model):
#     __tablename__ = 'interfaceSetting'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     modelPartId = db.Column(db.Integer, nullable=False)
#     jsonData = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class ClientServer(db.Model):
#     __tablename__ = 'clientServer'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     modelPartId = db.Column(db.Integer, nullable=False)
#     jsonData = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class WebClient(db.Model):
#     __tablename__ = 'webClient'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     modelPartId = db.Column(db.Integer, nullable=False)
#     jsonData = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class AppClient(db.Model):
#     __tablename__ = 'appClient'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     modelPartId = db.Column(db.Integer, nullable=False)
#     jsonData = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class IotDataCollect(db.Model):
#     __tablename__ = 'iotDataCollect'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     modelPartId = db.Column(db.Integer, nullable=False)
#     jsonData = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)
#
#
# class IotDataIssue(db.Model):
#     __tablename__ = 'iotDataIssue'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     modelPartId = db.Column(db.Integer, nullable=False)
#     jsonData = db.Column(db.JSON, nullable=True)
#     storage_time = db.Column(db.DateTime, default=datetime.now)


if __name__ == '__main__':
    # 删除数据库下的所有上述定义的表，防止重复创建
    with app.app_context():
        db.drop_all()
        # 将上述定义的所有表对象映射为数据库下的表单（创建表）
        db.create_all()
        # 向表中插入记录：实例化-插入-提交
        #     book1 = Book(title='人工智能导论', publishing_office='高等教育出版社', isbn='9787040479843')
        #     db.session.add(book1)
        db.session.commit()
