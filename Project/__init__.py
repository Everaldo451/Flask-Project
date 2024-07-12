from flask import Flask
from .application import views, auth
from .models.models import db

def create_app():
	
	app = Flask(__name__, instance_relative_config=True)
	
	app.config.from_pyfile("settings.py")
	
	app.register_blueprint(views.bp)
	app.register_blueprint(auth.at)

	
	
	db.init_app(app)
	
	with app.app_context():
		db.create_all()
	
	
	return app