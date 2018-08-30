from flask import request
from flask_restful import Resource
from models import UserModel


class UserCreate(Resource):
    def post(self):
        user = UserModel(
            username=request.form['username'],
            password=request.form['password'],
            name=request['name']
        )

        try:
            user.save_to_db()
            return {'message': 'user was successfully created'}, 200
        except Exception:
            return {'message': 'something went wrong'}, 500
