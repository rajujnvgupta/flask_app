from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from app.models import User, db
from app.schemas import UserSchema
from pydantic import ValidationError
import json

user_bp = Blueprint('user', __name__, url_prefix='/users')

# CREATE a new user
@user_bp.route('/', methods=['POST'])
def create_user():
    try:
        print('raju gupta', request.data)
        data = json.loads(request.data)

        print(data)
        user_data = UserSchema(**data)

        new_user = User(name=user_data.name, email=user_data.email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify(new_user.to_dict()), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User with this email already exists"}), 400

# READ all users
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# READ a single user by id
@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict()), 200

# UPDATE a user by id
@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        data = json.loads(request.data)
        user_data = UserSchema(**data)

        user = User.query.get_or_404(id)
        user.name = user_data.name
        user.email = user_data.email
        db.session.commit()

        return jsonify(user.to_dict()), 200
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

# DELETE a user by id
@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
