from flask import Flask

from app.routes.fixtures import fixtures_bp
from app.routes.frontend import frontend_bp
from app.routes.health import health_bp
from app.routes.stadiums import stadiums_bp
from app.routes.weather import weather_bp


def create_app() -> Flask:
	app = Flask(__name__)

	app.register_blueprint(health_bp)
	app.register_blueprint(stadiums_bp)
	app.register_blueprint(fixtures_bp)
	app.register_blueprint(weather_bp)
	app.register_blueprint(frontend_bp)

	return app
