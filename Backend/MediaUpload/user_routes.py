from flask import Blueprint, request, jsonify,Response
from models import User,Img,Video
from db import db

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/create_user', methods=['POST'])
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

@user_routes.route('/update_username/<string:username>', methods=['PUT'])
def update_username(username):
    user = User.query.filter_by(name=username).first()
    if not user:
        return 'User not found', 404

    data = request.get_json()
    new_username = data.get('new_username')

    if not new_username:
        return 'New username is required', 400

    # Check if the new username is already taken
    existing_user = User.query.filter_by(name=new_username).first()
    if existing_user:
        return 'Username is already taken', 409

    user.username = new_username
    db.session.commit()

    return jsonify({'message': 'Username updated successfully'})

@user_routes.route('/update_email/<string:username>', methods=['PUT'])
def update_email(username):
    user = User.query.filter_by(name=username).first()
    if not user:
        return 'User not found', 404

    data = request.get_json()
    new_email = data.get('new_email')

    if not new_email:
        return 'New email is required', 400

    # Check if the new email is already taken
    existing_user = User.query.filter_by(email=new_email).first()
    if existing_user:
        return 'Email is already taken', 409

    user.email = new_email
    db.session.commit()

    return jsonify({'message': 'Email updated successfully'})


@user_routes.route('/get_user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        return 'User not found', 404

    user_data = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }

    return jsonify(user_data)


@user_routes.route('/get_image/<string:username>/<int:image_id>', methods=['GET'])
def get_image_by_id(username, image_id):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    image = Img.query.filter_by(id=image_id, user_id=user.id).first()
    if image is None:
        return 'Image not found', 404

    return Response(image.img, content_type=image.mimetype)

@user_routes.route('/get_video/<string:username>/<int:video_id>', methods=['GET'])
def get_video_by_id(username, video_id):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    video = Video.query.filter_by(id=video_id, user_id=user.id).first()
    if video is None:
        return 'Video not found', 404

    return Response(video.video, content_type=video.mimetype)

@user_routes.route('/get_all_images/<string:username>', methods=['GET'])
def get_all_images(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    images = Img.query.filter_by(user_id=user.id).all()

    image_list = []
    for img in images:
        image_data = {
            'id': img.id,
            'name': img.name,
            'mimetype': img.mimetype,
            # You can add more image details as needed
        }
        image_list.append(image_data)

    return jsonify(image_list)

@user_routes.route('/get_all_videos/<string:username>', methods=['GET'])
def get_all_videos(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    videos = Video.query.filter_by(user_id=user.id).all()

    video_list = []
    for vid in videos:
        video_data = {
            'id': vid.id,
            'name': vid.name,
            'mimetype': vid.mimetype,
            # You can add more video details as needed
        }
        video_list.append(video_data)

    return jsonify(video_list)


@user_routes.route('/delete_image/<string:username>/<int:image_id>', methods=['DELETE'])
def delete_image_by_id(username, image_id):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    image = Img.query.filter_by(id=image_id, user_id=user.id).first()
    if image is None:
        return 'Image not found', 404

    db.session.delete(image)
    db.session.commit()

    return 'Image deleted', 200

@user_routes.route('/delete_video/<string:username>/<int:video_id>', methods=['DELETE'])
def delete_video_by_id(username, video_id):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    video = Video.query.filter_by(id=video_id, user_id=user.id).first()
    if video is None:
        return 'Video not found', 404

    db.session.delete(video)
    db.session.commit()

    return 'Video deleted', 200



@user_routes.route('/delete_all_images/<string:username>', methods=['DELETE'])
def delete_all_images(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    # Find all images associated with the user
    images = Img.query.filter_by(user_id=user.id).all()

    for image in images:
        db.session.delete(image)

    db.session.commit()

    return 'All images deleted', 200

@user_routes.route('/delete_all_videos/<string:username>', methods=['DELETE'])
def delete_all_videos(username):
    user = User.query.filter_by(name=username).first()
    if user is None:
        return 'User not found', 404

    # Find all videos associated with the user
    videos = Video.query.filter_by(user_id=user.id).all()

    for video in videos:
        db.session.delete(video)

    db.session.commit()

    return 'All videos deleted', 200
