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
