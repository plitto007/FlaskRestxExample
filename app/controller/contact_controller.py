import logging
from flask import request, jsonify, send_from_directory
from flask_restx import Resource
from ..util.dto import ContactDto
from ..util.data_util import build_json_result
import uuid

api = ContactDto.api


@api.route("/list")
class ContactList(Resource):
    @api.response(200, "get contact list")
    @api.doc("upload photo")
    def post(self):
        print('Upload photo')
        print('data: {}'.format(request.data))
        print('param: {}'.format(request.args))
        data = request.form
        phone = data.get('phone')
        start = data.get('start') or 0
        length = int(data.get('length') or 10)
        data = []
        for i in range(0, length):
            data.append({
                "id": uuid.uuid4().__str__(),
                "phone": "01656228578",
                "admin_id": "231313123123",
                "avatar": "https://cdb.boxhoidap.com/cdbjp/r_phim-hoat-hinh-kattobi-itto--7889f52b11440908a3cf6f2055e1ffdc.wepb",
                "is_login": False,
                "user_name": "super_admin",
                "data_unread_message_count": 0,
                "last_message": {
                    "user_id": uuid.uuid4().__str__(),
                    "message": "123",
                    "message_type": "001"
                }
            })
        response = {
            "code": 200,
            "success": "true",
            "data": data,
        }
        return response, 200
