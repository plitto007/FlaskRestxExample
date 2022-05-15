from flask_restx import Namespace, fields


class UploadDto:
    api = Namespace("upload", description="Upload DTO")


class UserDto:
    api = Namespace("user", description="API for user")


class ContactDto:
    api = Namespace("contact", description="API for user")


class MessagesDto:
    api = Namespace("messages", description="API for Message")
