from flask import Blueprint, request, jsonify
from models import Img,User
from db import db
from werkzeug.utils import secure_filename

img_routes = Blueprint('image_routes', __name__)

@img_routes.route('/upload_image/<string:username>', methods=['POST'])
def upload_image(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    image_file = request.files['image']
    if not image_file:
        return 'No image uploaded!', 400

    filename = secure_filename(image_file.filename)
    mimetype = image_file.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Img(img=image_file.read(), name=filename, mimetype=mimetype, user_id=user.id)
    db.session.add(img)
    db.session.commit()

    return 'Image Uploaded!', 200

@img_routes.route('/update_image/<string:username>/<int:image_id>', methods=['PUT'])
def update_image(username, image_id):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    image = Img.query.filter_by(id=image_id, user_id=user.id).first()
    if image is None:
        return 'Image not found', 404

    new_image_file = request.files['new_image']
    if not new_image_file:
        return 'No new image uploaded!', 400

    filename = secure_filename(new_image_file.filename)
    mimetype = new_image_file.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    # Update the image data, name, and mimetype
    image.img = new_image_file.read()
    image.name = filename
    image.mimetype = mimetype

    db.session.commit()

    return 'Image Updated!', 200
