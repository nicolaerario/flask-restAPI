from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# until SQLAlchemy set it to False by default
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return jsonify(message="Hello World Flask Rest API"), 200


@app.route("/not_found")
def not_found():
    return jsonify(message="Resource not found"), 404


# Database models
class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)


class Domain(db.Model):
    __tablename__ = "domains"
    domain_id = Column(Integer, primary_key=True)
    domain_name = Column(String)
    domain_type = Column(String)
    registered_on = Column(String)
