from flask import Flask, Blueprint
from flask_restx import Api
from config import Config
from app.util import data_util

contacts = None
messages = None


def create_app(config_class=Config):
    global contacts, messages
    app = Flask(__name__)
    register_blueprints(app)
    data_util.generate_data()
    data_util.generate_chat_room_msgs()
    contacts = data_util.load_data()
    messages = data_util.load_data("app/raw/chat.json")

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
    from app.controller.user_controller import api as user_ns
    from app.controller.messages_controller import api as message_ns
    api.add_namespace(upload_ns)
    api.add_namespace(contact_ns)
    api.add_namespace(user_ns)
    api.add_namespace(message_ns)
    app.register_blueprint(blueprint)
