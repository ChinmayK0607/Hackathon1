from flask import Flask, request, Response,jsonify
from werkzeug.utils import secure_filename

from db import db_init, db
from models import Img,Video,User

from user_routes import user_routes
from image_routes import img_routes
from video_routes import video_routes
app = Flask(__name__)

app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(img_routes, url_prefix='/img')
app.register_blueprint(video_routes, url_prefix='/vid')


#url here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route("/")
def hello_world():
    return "Hello World!"
if __name__ == '__main__':
    app.run(debug=True,port = 8000)
