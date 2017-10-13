from django.db import models

from mongoengine import *
import charts
import json
# from models import ask_rent,rent_fang

connect('ganji',host='127.0.0.1',port = 27017)


class ask_rent(Document):
    title = StringField(required=True)
    price = StringField(required=True)
    time = StringField(max_length=25)
    address = ListField(required=True)
    fang = IntField(required=True)
    href = StringField(required=True)


class rent_fang(Document):
    fang = IntField(required=True)
    title = StringField(required=True)
    price = IntField(required=True)
    address = ListField(required=True)
    info = ListField(required=True)
    href = StringField(required=True)
    time = StringField(max_length=25)

class second_fang(Document):
    fang = IntField(required=True)
    title = StringField(required=True)
    price = IntField(required=True)
    address = ListField(required=True)
    info = ListField(required=True)
    href = StringField(required=True)
    time = StringField(max_length=25)

class business_fang(Document):
    fang = IntField(required=True)
    title = StringField(required=True)
    price = IntField(required=True)
    address = ListField(required=True)
    info = ListField(required=True)
    href = StringField(required=True)
    time = StringField(max_length=25)

class price_pre(Document):
    fang = StringField(required=True)
    price = FloatField(required=True)
    total = IntField(required=True)


