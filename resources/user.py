import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

		
# Resource class for registering an user.		
class UserRegister(Resource):
	
	# Define a parser to accept only username and password as parameters.
	parser = reqparse.RequestParser()
	parser.add_argument('username', type = str, required = True, help = 'This field cannot be blank')
	parser.add_argument('password', type = str, required = True, help = 'This field cannot be blank')
	
	def post(self):
		# Use the parser to read the incoming JSON data.
		data = UserRegister.parser.parse_args()
		# If the user is already present in the DB, return an error.
		if UserModel.find_by_username(data['username']):
			return {'message' : 'A user with that username already exists'}, 400
		# Create an user object and write it to the table using SQLAlchemy.
		user = UserModel(**data)
		user.save_to_db()
		
		return {"message" : "user created successfully"}, 201
