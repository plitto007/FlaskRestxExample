import logging
from flask import request, jsonify, send_from_directory
from flask_restx import Resource
from ..services.upload_service import upload
from app.util.dto import UserDto
from werkzeug.datastructures import FileStorage

api = UserDto.api
UPLOAD_DIRECTORY = "app/download"
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


@api.route('/fileUpload')
class UploadPhoto(Resource):
    @api.response(200, "Upload photo succeed")
    @api.doc("upload photo")
    def post(self):
        print('Upload photo')
        return upload(request, 'photo')
