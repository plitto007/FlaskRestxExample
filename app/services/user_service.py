import logging
from flask import request, jsonify, send_from_directory
from flask_restx import Resource
from app.util.dto import UserDto

api = UserDto.api

@api.route('/contact')
class UploadPhoto(Resource):
    @api.response(200, "Upload photo succeed")
    @api.doc("upload photo")
    def post(self):
        print('Upload photo')
        return upload(request, 'photo')
