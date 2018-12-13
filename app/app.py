'''return 一个 app，避免循环引用'''

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

