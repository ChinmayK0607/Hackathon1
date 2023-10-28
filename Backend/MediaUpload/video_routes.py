# video_routes.py

from flask import Blueprint, request
from werkzeug.utils import secure_filename
from models import User, Video
from db import db

video_routes = Blueprint('video_routes', __name__)

@video_routes.route('/upload_video/<string:username>', methods=['POST'])
def upload_video(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    video_file = request.files['video']
    if not video_file:
        return 'No video uploaded!', 400

    filename = secure_filename(video_file.filename)
    mimetype = video_file.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    video = Video(video=video_file.read(), name=filename, mimetype=mimetype, user_id=user.id)
    db.session.add(video)
    db.session.commit()

    return 'Video Uploaded!', 200

@video_routes.route('/update_video/<string:username>/<int:video_id>', methods=['PUT'])
def update_video(username, video_id):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    video = Video.query.filter_by(id=video_id, user_id=user.id).first()
    if video is None:
        return 'Video not found', 404

    new_video_file = request.files['new_video']
    if not new_video_file:
        return 'No new video uploaded!', 400

    filename = secure_filename(new_video_file.filename)
    mimetype = new_video_file.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    # Update the video data, name, and mimetype
    video.video = new_video_file.read()
    video.name = filename
    video.mimetype = mimetype

    db.session.commit()

    return 'Video Updated!', 200
