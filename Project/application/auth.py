from flask import Blueprint, make_response, session, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.models import db, User
from smtplib import SMTP


at = Blueprint("auth",__name__,url_prefix="/auth")



@at.before_request
def before():
	if session.get("id"):
		return redirect(url_for('bp.home'))
		
	return None
	
	
	
	
	


@at.route("/login",methods=["POST"])
def login():
	
	print(request.form)
	
	if request.form:
		
		print(request.form)
		
		users = User.query.all()
		db.session.delete(users[1])
		db.session.commit()
		
		user = User.query.filter_by(email=request.form.get("email")).first()
		
		if user and check_password_hash(request.form.get("password"),user.password):
			
			session["id"] = user.id
			
			return redirect(url_for("bp.home"))
		
		else:
			
			flash("Usuario ou senha inválidos","login_error")
			
			return redirect(url_for("bp.login"))
	
	return redirect(url_for("bp.login"))
	
	
	
	
	
	
	
	
@at.route("/register",methods=["POST"])
def register():
	
	if request.form:
		
		conta = User.query.filter_by(email=request.form.get("email")).first() or User.query.filter_by(username=request.form.get("username")).first()
		
		if conta:
			
			flash("Usuario já cadastrado","register_error")
			
			return  redirect(url_for("bp.login"))
			
		user = User(username = request.form.get("username"),email=request.form.get("email"),password=generate_password_hash(request.form.get("password")))
		
		db.session.add(user)
		db.session.commit()
		
		session["id"] = user.id
	
	
	return redirect(url_for('bp.home'))
	