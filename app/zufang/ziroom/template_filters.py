import time
from app.app import app

@app.template_filter('int2time')
def int2time(timestamp):
    if isinstance(timestamp, int):
        timeArray = time.localtime(timestamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return ''

@app.template_filter('imgsrc')
def imgsrc(img):
    if isinstance(img, dict) and 'path' in img and 'origin_src' in img:
        if img['path']:
            return img['path'].replace('/home/py3/data', '/static')
        elif img['origin_src']:
            return img['origin_src']
        else:
            return '#'

@app.template_filter('shi_fou')
def imgsrc(value):
    if value == None:
        return ''
    return '是' if value else '否'