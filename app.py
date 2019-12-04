from flask import Flask

from models import db
from routes import api

app = Flask(__name__)
app.register_blueprint(api)
db.init_app(app)

if __name__ == '__main__':
    app.run()
