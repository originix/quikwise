import json
import os

from .custom_responses import CustomResponse
from django.utils.deconstruct import deconstructible
from rest_framework.views import exception_handler
from uuid import uuid4


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s/%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        # extension = os.path.splitext(filename)[1]
        return self.path % (uuid4(), filename)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    data = CustomResponse()

    if response is not None:
        response.data['status_code'] = response.status_code

        return data.response_exception_handler(response)


class JsonValidation():

    @staticmethod
    def is_json(json_data=None):
        try:
            json.loads(json_data)
        except ValueError:
            return False
        return True
