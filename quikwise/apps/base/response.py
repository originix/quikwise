from rest_framework.response import Response as BaseResponse


class Response(BaseResponse):

    def __init__(self, data=None, template_name=None, status=None, headers=None, exception=False, content_type=None, message='success', errors=None, meta=None):
        super().__init__(data, status, template_name, headers, exception, content_type)

        self.message = message
        self.errors = errors
        self.meta = meta

        self.data = self.custom_data()

        print(self.data)

    def custom_data(self):
        data = {'message': self.message, 'data': self.data}

        if self.errors:
            data['errors'] = self.errors
            del data['data']

        if self.meta:
            data['meta'] = self.meta

        return data
