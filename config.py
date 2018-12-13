import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'jsoiafjhojnsaofwjesldfjhoisa'

MONGODB_SETTINGS = {
    'host': 'your host',
    'port': 27017,          # 注意该为 int 类型
    'username': 'your username',
    'password': 'your passwd',
    'connect': False,
}