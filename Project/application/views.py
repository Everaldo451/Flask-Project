from flask import Blueprint, render_template, make_response, session
from ..models.models import db, User

bp = Blueprint('bp',__name__,url_prefix="/")

@bp.context_processor
def processor():
	if session.get("id"):
		user = User.query.filter_by(id=int(session.get("id"))).first()
		return {"user":user}
	return {"user":None}


@bp.route("/",methods=["GET"])
def home():
	
	return render_template("home.html")
	
@bp.route("/login",methods=["GET"])
def login():
	
	return render_template("login.html")

