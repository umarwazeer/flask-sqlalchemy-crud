from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_migrate import Migrate

from app import  db




class Employee(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(220), nullable=False)
    email = db.Column(db.String(400), unique=True, nullable=False)
    # fname = db.Column(db.String(400), unique=True, nullable=False)
    salary = db.Column(db.Integer, unique=False, nullable=False)
    # experience = db.Column(db.String(400), unique=True, nullable=False)
    role = db.Column(db.String(400), unique=False, nullable=False)
    gender = db.Column(db.String(400), unique=False, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    # dep_id = db.Column(db.Integer, db.ForeignKey('department.dep_id'))
    # attan = db.relationship('Attandence', backref='emp', lazy=True)
    # d_of_join = db.Column(db.String(400), unique=True, nullable=False)
    # d_of_birth = db.Column(db.String(400), unique=True, nullable=False)
    # qualifiucations = db.Column(db.String(400), unique=False, nullable=False)

    def __str__(self):
        return {'name':self.name}


class User(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(220), nullable=False)
    email = db.Column(db.String(400), unique=True, nullable=False)
    # dep_id = db.Column(db.Integer, db.ForeignKey('department.id'))
