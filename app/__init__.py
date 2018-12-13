from app.app import app
from app.main import main
from app.zufang.ziroom import zufang_ziroom

app.register_blueprint(main)
app.register_blueprint(zufang_ziroom, url_prefix='/zufang/ziroom')

