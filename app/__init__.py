from flask import Flask, Blueprint
from flask_restx import Api
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api = Api(blueprint,
              title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
              version='1.0',
              description='a boilerplate for flask restplus web service'
              )
    from app.controller.upload_controller import api as upload_ns
    from app.controller.contact_controller import api as contact_ns
    api.add_namespace(upload_ns)
    api.add_namespace(contact_ns)
    app.register_blueprint(blueprint)
