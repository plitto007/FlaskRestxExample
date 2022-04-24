import os

from werkzeug.utils import secure_filename

from ..util.data_util import build_json_result
import werkzeug
from werkzeug.datastructures import FileStorage

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'app/download'


def upload(request, media_type):
    if media_type == 'photo':
        return upload_photo(request)
    if media_type == 'video':
        return upload_video(request)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_photo(request):
    print('request.files: {}'.format(request.files))
    if 'file' not in request.files:
        return build_json_result(None, 400, 'This file is not valid', 'This file is not valid')
    #
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == "":
        return build_json_result(None, 406, 'Please select a file', 'Please select a file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        response_object = {
            'fileName': str(filename)
        }
        return build_json_result(response_object, 200, 'upload success', 'upload success')
    else:
        return build_json_result(None, 403, 'This file is not valid', 'This file is not valid')


def upload_video(request):
    if 'file' not in request.files:
        return build_json_result(None, 400, 'This file is not valid', 'This file is not valid')
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == "":
        return build_json_result(None, 406, 'Please select a file', 'Please select a file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        response_object = {
            'fileName': str(filename)
        }
        return build_json_result(response_object, 200, 'upload success', 'upload success')
    else:
        return build_json_result(None, 403, 'This file is not valid', 'This file is not valid')
