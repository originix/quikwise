import os

from django.utils.deconstruct import deconstructible
from uuid import uuid4


@deconstructible
class RandomFileName(object):
    def __init__(self, path):
        self.path = os.path.join(path, "%s/%s")

    def __call__(self, _, filename):
        # @note It's up to the validators to check if it's the correct file type in name or if one even exist.
        # extension = os.path.splitext(filename)[1]
        return self.path % (uuid4(), filename)