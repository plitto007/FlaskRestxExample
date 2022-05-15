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
            start = 0

        start_range = start
        print('revert: {}'.format(revert))
        print('size: {}'.format(size))
        if revert == 1:
            print('calculating end range revert')
            end_range = start_range - size - 1
            if end_range < 0:
                end_range = 0
        else:
            end_range = start_range + size - 1
            print('endrange: {}'.format(end_range))
            if end_range > MESSAGE_COUNT:
                end_range = MESSAGE_COUNT
        print('range: {}->{}'.format(start_range, end_range))
        from app import messages
        for i in range(start_range, end_range, -1 if revert == 1 else 1):
            data.append(messages[i])

        response = {
            "code": 200,
            "success": "true",
            "data": data,
        }
        return response, 200
