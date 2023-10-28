from flask import Flask, request, Response,jsonify
from werkzeug.utils import secure_filename

from db import db_init, db
from models import Img,Video

app = Flask(__name__)
#url here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Img(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

    return 'Img Uploaded!', 200


@app.route('/<int:id>')
def get_img(id):
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)
@app.route('/update_img/<int:id>', methods=['POST'])
def update_img(id):
    # Check if the image with the given ID exists in the database
    img = Img.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    # Get the new image from the request
    new_pic = request.files['new_pic']
    if not new_pic:
        return 'No new image uploaded!', 400

    # Update the image data, name, and mimetype
    img.img = new_pic.read()
    img.name = secure_filename(new_pic.filename)
    img.mimetype = new_pic.mimetype

    # Commit the changes to the database
    db.session.commit()

    return 'Img Updated!', 200


@app.route('/upload_video', methods=['POST'])
def upload_video():
    video = request.files['video']
    if not video:
        return 'No video uploaded!', 400

    filename = secure_filename(video.filename)
    mimetype = video.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    video_data = video.read()

    video = Video(video=video_data, name=filename, mimetype=mimetype)
    db.session.add(video)
    db.session.commit()

    return 'Video Uploaded!', 200

@app.route('/videos/<int:id>')
def get_video(id):
    video = Video.query.filter_by(id=id).first()
    if not video:
        return 'Video Not Found!', 404

    return Response(video.video, mimetype=video.mimetype)

@app.route('/update_video/<int:id>', methods=['PUT'])
def update_video(id):
    video = Video.query.filter_by(id=id).first()
    if not video:
        return 'Video Not Found!', 404

    new_video = request.files['new_video']
    if not new_video:
        return 'No new video uploaded!', 400

    filename = secure_filename(new_video.filename)
    mimetype = new_video.mimetype

    video.video = new_video.read()
    video.name = filename
    video.mimetype = mimetype

    db.session.commit()

    return 'Video Updated!', 200

@app.route('/videos', methods=['GET'])
def get_all_videos_with_titles():
    videos = Video.query.all()
    video_list = []
    for video in videos:
        video_list.append({'id': video.id, 'title': video.name})
    return jsonify(video_list)

def create_user():
    # Extract user data from the request
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return 'Name and email are required fields.', 400

    # Check if the user with the same email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return 'User with this email already exists.', 409

    # Create a new user
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})
if __name__ == '__main__':
    app.run(debug=True,port = 8000)
