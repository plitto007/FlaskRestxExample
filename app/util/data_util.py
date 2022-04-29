import json
import uuid


def build_json_result(data, code=200, message='ok', db_message='ok'):
    if type(data) is list:
        data = list2dict(data)
    else:
        data = row2dict(data)
    result = {
        "meta": {
            "code": code,
            "message": message,
            "db_message": db_message
        },
        "data": data
    }
    return result, code


def list2dict(lst):
    result = []
    for row in lst:
        result.append(row2dict(row))
    return result


def row2dict(row):
    if not row:
        return row
    if type(row) is tuple:
        return row
    if type(row) is dict:
        return row
    if type(row) in (int, float, bool, str):
        return row
    d = {}
    for column in row.__table__.columns:
        if column.name != 'password_hash':
            if getattr(row, column.name) == None:
                d[column.name] = None
            else:
                if type(getattr(row, column.name)) is int:
                    d[column.name] = int(getattr(row, column.name))
                else:
                    if type(getattr(row, column.name)) is bool:
                        d[column.name] = bool(getattr(row, column.name))
                    else:
                        d[column.name] = str(getattr(row, column.name))


def load_data(path='app/raw/contact.json'):
    file = open(path, "r")
    string = file.read()
    file.close()
    return json.loads(string)


def generate_data(path='app/raw/contact.json'):
    with open(path, "w") as file:
        data = []
        for i in range(0, 235):
            item = {
                "id": i,
                "phone": "01656228578",
                "admin_id": "231313123123",
                "avatar": "https://cdb.boxhoidap.com/cdbjp/r_phim-hoat-hinh-kattobi-itto--7889f52b11440908a3cf6f2055e1ffdc.wepb",
                "is_login": False,
                "user_name": "user {}".format(i),
                "data_unread_message_count": 0,
                "last_message": {
                    "user_id": uuid.uuid4().__str__(),
                    "message": "123",
                    "message_type": "001"
                }
            }
            data.append(item)
        file.write(json.dumps(data))
        file.close()
