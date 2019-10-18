from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# until SQLAlchemy set it to False by default
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database CLI commands utilities
@app.cli.command("db_create")
def db_create():
    db.create_all()
    print("Database created!")


@app.cli.command("db_drop")
def db_drop():
    db.drop_all()
    print("Database dropped!")


@app.cli.command("db_seed")
def db_seed():
    google = Domain(
        domain_name="Google.com", domain_type="Search Engine", registered_on="1997"
    )
    yahoo = Domain(
        domain_name="Yahoo.com", domain_type="Internet services", registered_on="1994"
    )
    amazon = Domain(
        domain_name="Amazon.com", domain_type="e-Commerce", registered_on="1994"
    )
    db.session.add(google)
    db.session.add(yahoo)
    db.session.add(amazon)

    test_user = User(
        first_name="Paperino",
        last_name="Paolino",
        email="paperino@topolinia.com",
        password="my_str0ngPassword",
    )
    db.session.add(test_user)
    db.session.commit()
    print("Database seeded!")


# App Routes
@app.route("/")
def hello_world():
    return jsonify(message="Hello World Flask Rest API"), 200


@app.route("/not_found")
def not_found():
    return jsonify(message="Resource not found"), 404


@app.route("/domains", methods=["GET"])
def domains():
    domains_list = Domain.query.all()
    return jsonify(domains_schema.dump(domains_list))


# Database models and schema
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


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "first_name", "last_name", "email", "password")


class DomainSchema(ma.Schema):
    class Meta:
        fields = ("domain_id", "domain_name", "domain_type", "registered_on")


user_schema = UserSchema()
users_schema = UserSchema(many=True)

domain_schema = DomainSchema()
domains_schema = DomainSchema(many=True)
