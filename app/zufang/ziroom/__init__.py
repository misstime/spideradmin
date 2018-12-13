from flask import Blueprint
from app.zufang.ziroom.template_filters import *

zufang_ziroom = Blueprint('zufang_ziroom', __name__)

from . import views