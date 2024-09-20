from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
def create_app():
    config = Config()
    app = Flask(__name__)
    # CONFIG = Config()
    app.config.from_object(config)

    # app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///test.db'
    # app.config('SQLALCHEMY_TRACK_MODIFICATIONS') = False
    Migrate(app, db)
    db.init_app(app)

    # Middleware
    from .middleware import before_request_logging, after_request_logging
    app.before_request(before_request_logging)
    app.after_request(after_request_logging)

    # Register Blueprints
    from .route import user_bp
    app.register_blueprint(user_bp)

    return app