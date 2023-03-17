import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import SQLconnect.DBconfig
from datetime import datetime

app = Flask(__name__)
ACCOUNTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "accounts.json")
app.config.from_object(SQLconnect.DBconfig)
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)


class ModelPart(db.Model):
    __tablename__ = 'modelPart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    quote = db.Column(db.String(50), nullable=False)
    quoted = db.Column(db.String(50), nullable=False)


class ServerSideData(db.Model):
    __tablename__ = 'serverSide'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelPartId = db.Column(db.Integer, nullable=False)
    jsonData = db.Column(db.JSON, nullable=True)


class InterfaceSetting(db.Model):
    __tablename__ = 'interfaceSetting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelPartId = db.Column(db.Integer, nullable=False)
    jsonData = db.Column(db.JSON, nullable=True)


class ClientServer(db.Model):
    __tablename__ = 'clientServer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelPartId = db.Column(db.Integer, nullable=False)
    jsonData = db.Column(db.JSON, nullable=True)


class WebClient(db.Model):
    __tablename__ = 'webClient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelPartId = db.Column(db.Integer, nullable=False)
    jsonData = db.Column(db.JSON, nullable=True)


class AppClient(db.Model):
    __tablename__ = 'appClient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelPartId = db.Column(db.Integer, nullable=False)
    jsonData = db.Column(db.JSON, nullable=True)


class IotDataCollect(db.Model):
    __tablename__ = 'iotDataCollect'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelPartId = db.Column(db.Integer, nullable=False)
    jsonData = db.Column(db.JSON, nullable=True)


class IotDataIssue(db.Model):
    __tablename__ = 'iotDataIssue'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modelPartId = db.Column(db.Integer, nullable=False)
    jsonData = db.Column(db.JSON, nullable=True)
