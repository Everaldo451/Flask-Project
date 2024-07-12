from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
	pass


db = SQLAlchemy(model_class=Base)


class User(db.Model):
	
	id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
	username = db.Column("username", db.String(150))
	email = db.Column("email", db.String(150))
	password = db.Column("password", db.String(2000))
	
	
	def __init_(self,id,username,email,password):
		
		self.id = id
		self.username = username
		self.email = email
		self.password = password