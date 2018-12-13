from flask_mongoengine import MongoEngine
from app.app import app

app.config['MONGODB_SETTINGS']['db'] = 'zufang'
db = MongoEngine()
db.init_app(app)

class Ziroom(db.Document):

    meta = {
        'strict': False,
    }

    room_id = db.IntField()
    air = db.DictField()
    allocation = db.DictField()
    area = db.IntField()
    city = db.StringField()
    community = db.StringField()
    district = db.StringField()
    floor = db.ListField()
    heating = db.StringField()
    house_id = db.IntField()
    house_type = db.ListField()
    is_first_rent = db.BooleanField()
    is_near_subway = db.BooleanField()
    is_private_balcony = db.BooleanField()
    is_private_bathroom = db.BooleanField()
    keeper = db.DictField()
    map_position = db.ListField()
    payment = db.DictField()
    photos = db.ListField()
    price = db.DictField()
    product = db.StringField()
    rent_type = db.StringField()
    room_link = db.StringField()
    room_name = db.StringField()
    room_sn = db.StringField()
    room_style = db.StringField()
    roommates = db.ListField()
    sub_district = db.StringField()
    subway = db.ListField()
    title_thumb = db.DictField()
    towards = db.StringField()
    room_introduce = db.StringField()
    rent_status = db.StringField()
    uptime = db.IntField()

