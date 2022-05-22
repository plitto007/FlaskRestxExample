import logging
from flask import request, jsonify, send_from_directory
from flask_restx import Resource
from ..util.dto import MessagesDto
from ..util.data_util import build_json_result
import uuid
import time

api = MessagesDto.api

MESSAGE_COUNT = 245


@api.route("/room_message")
class RoomMessages(Resource):
    """
    Load messages of room with room id
    """

    @api.response(200, "get messages done")
    @api.doc("Room messages")
    def post(self):
        print('Message LIST')
        print('param: {}'.format(request.form))

        data = request.form
        start = int(data.get('start') or 0)
        size = int(data.get('size') or 50)
        revert = int(data.get('revert') or 0)

        data = []
        if start < 0:
            if revert == 1:
                start_range = MESSAGE_COUNT - 1
            else:
                start_range = 0

        else:
            if revert == 1:
                start_range = MESSAGE_COUNT - start - 1
            else:
                start_range = start

        print('revert: {}'.format(revert))
        print('size: {}'.format(size))
        if revert == 1:
            print('calculating end range revert')
            end_range = start_range - size
            if end_range < -1:
                end_range = -1
        else:
            end_range = start_range + size
            print('endrange: {}'.format(end_range))
            if end_range > MESSAGE_COUNT:
                end_range = MESSAGE_COUNT
        print('range: {}->{}'.format(start_range, end_range))

        from app import messages
        if start_range >= MESSAGE_COUNT:
            print("return empty due to full")
        else:
            for i in range(start_range, end_range, -1 if revert == 1 else 1):
                data.append(messages[i])

        member_name = [
            {
                "id": "5b5744223900632c5739b97d",
                "phone": "01649083327",
                "avatar": "https://chat.secureiot.com.vn:8008/images/profile.png",
                "login_flg": True,
                "user_name": "client9"
            }
        ]
        user_read = [
            "5b5744223900632c5739b97d"
        ]
        room_id = "449f39fe-bc2f-4a3a-a91f-a41a1475e320"
        response = {
            "success": True,
            "log_messages": data,
            "member_name": member_name,
            "room_id": room_id,
            "user_read": user_read,
            "admin_id": "5b5744223900632c5739b97d"
        }

        return response, 200
