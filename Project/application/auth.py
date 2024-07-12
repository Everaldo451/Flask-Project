from flask import Blueprint, session, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..models.models import db, User
from smtplib import SMTP


at = Blueprint("auth",__name__,url_prefix="/auth")



@at.before_request
def before():
	if session.get("id") and request.endpoint != "auth.logout":
		return redirect(url_for('bp.home'))
	
	
	


@at.route("/login",methods=["POST"])
def login():
	
	if request.form:
		
		user = User.query.filter_by(email=request.form.get("email")).first()
		
		if user and check_password_hash(user.password,request.form.get("password")):
			
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





@at.route("/logout",methods=["GET"])
def logout():

	if session.get("id"):

		session.pop("id")
		session.clear()

		return redirect(url_for('bp.home'))

	return redirect(url_for('bp.home'))
	