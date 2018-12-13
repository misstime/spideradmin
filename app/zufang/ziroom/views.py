import math
from flask import render_template
from flask import request
from . import zufang_ziroom
from .models import Ziroom

@zufang_ziroom.route('/', methods=['GET','POST'])
@zufang_ziroom.route('/index', methods=['GET','POST'])
def index():
    page = 1
    per_page = 5
    try:
        page = int(request.args.get('page'))
    except:
        pass

    search_raw = {}
    city = request.form.get('city')
    room_name = request.form.get('room_name')
    if city and city != '全部':
        search_raw['city'] = city
    if room_name:
        search_raw['room_name'] = {'$regex': room_name}

    pagination = Ziroom.objects(__raw__=search_raw).order_by('-uptime').paginate(page=page, per_page=per_page)
    pagination.total_page = math.ceil(pagination.total/per_page)
    return render_template(
        'zufang/ziroom/index.html',
        city = city,
        room_name = room_name,
        rooms = pagination.items,
        pagination = pagination,
        page_title = '租房 - 自如 - 列表页'
    )


@zufang_ziroom.route('/detail')
def detail():
    room_id = request.args.get('room_id')
    if not room_id.isdigit():
        return 'invalid prarams, access denedy !'
    else:
        room = Ziroom.objects(room_id=int(room_id)).get_or_404()
        return render_template(
            'zufang/ziroom/detail.html',
            room = room,
            page_title = '租房 - 自如 - 详情页'
        )






