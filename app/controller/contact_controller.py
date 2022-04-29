import logging
from flask import request, jsonify, send_from_directory
from flask_restx import Resource
from ..util.dto import ContactDto
from ..util.data_util import build_json_result
import uuid
import time
api = ContactDto.api

CONTACT_COUNT = 234


@api.route("/list")
class ContactList(Resource):
    @api.response(200, "get contact list")
    @api.doc("Contact list")
    def post(self):
        print('CONTACT LIST')
        # print('header: {}'.format(request.headers))
        print('data: {}'.format(request.data))
        print('param: {}'.format(request.args))
        data = request.form
        phone = data.get('phone')
        start = int(data.get('start') or 0)
        length = int(data.get('length') or 10)
        data = []
        print("phone: {} start: {} length: {}".format(phone, start, length))
        time.sleep(3)
        if start < CONTACT_COUNT:
            from app import contacts
            end_index = start + length - 1
            if end_index > CONTACT_COUNT - 1:
                end_index = CONTACT_COUNT - 1

            for i in range(start, end_index + 1):
                data.append(contacts[i])
                # data.append({
                #     "id": uuid.uuid4().__str__(),
                #     "phone": "01656228578",
                #     "admin_id": "231313123123",
                #     "avatar": "https://cdb.boxhoidap.com/cdbjp/r_phim-hoat-hinh-kattobi-itto--7889f52b11440908a3cf6f2055e1ffdc.wepb",
                #     "is_login": False,
                #     "user_name": "super_admin",
                #     "data_unread_message_count": 0,
                #     "last_message": {
                #         "user_id": uuid.uuid4().__str__(),
                #         "message": "123",
                #         "message_type": "001"
                #     }
                # })

        print("response data count: {}".format(len(data)))
        response = {
            "code": 200,
            "success": "true",
            "data": data,
        }
        return response, 200
