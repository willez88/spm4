from django.db import models
from mongoengine import *
from spm4.settings import db_name
# Create your models here.
connect(db_name)

class Persona(Document):
    _id = ObjectIdField()
    nombres = StringField(max_length=100)
    apellido = StringField(max_length=100)
    edad = IntField()

class Persona2(Document):
    nombre = StringField(max_length=100)
    apellido = StringField(max_length=100)
    cedula = StringField(max_length=100)
    edad = IntField()
