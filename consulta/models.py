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

class Estrella(Document):
    spmid = StringField(max_length=20)
    ra = FloatField()
    dec = FloatField()
    era = FloatField()
    edec = FloatField()
    pma = FloatField()
    pmd = FloatField()
    epma = FloatField()
    epmd = FloatField()
    b = FloatField()
    v = FloatField()
    ibiv = IntField()
    epav = FloatField()
    ep1 = FloatField()
    ep2 = FloatField()
    mp = IntField()
    np = IntField()
    nc = IntField()
    igalicat = IntField()
    j = FloatField()
    h = FloatField()
    k = FloatField()
