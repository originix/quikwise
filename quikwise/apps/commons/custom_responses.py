from rest_framework import status
from rest_framework.response import Response


class CustomResponse:

    def custom_response(self, success=True, messages='', data='', total=0):
        response = {}
        response['success'] = success
        response['messages'] = messages
        response['data'] = data
        response['total'] = total

        return response

    def custom_response_meta_links(self, success, messages, data, total, meta, links):
        response = {}
        response['success'] = success
        response['messages'] = messages
        response['data'] = data
        response['total'] = total
        response['meta'] = meta
        response['links'] = links

        return response

    def set_errors(self, errors):
        errors_text = ""
        for data in errors:
            errors_text += "{}\n\r".format(str(errors[data]).split("'")[1])

        return errors_text

    def set_errors_exception_handler(self, e):
        if e.get('detail'):
            return e.get('detail')
        else:
            errors = e.copy()
            del errors['status_code']
            errors_text = ""
            for data in errors:
                if data == "non_field_errors":
                    errors_text += "{}\n\r".format(str(errors[data]).split("'")[1])
                else:
                    errors_text += "{}: {}\n\r".format(data, str(errors[data]).split("'")[1])

            if errors_text[-2:] == '\n\r':
                errors_text = errors_text[:-2]

            return errors_text

    def response_custom_list_success(self, data):
        data = self.custom_response(data=data, total=len(data))

        return Response(data=data, status=status.HTTP_200_OK)

    def response_jwt_custom_success(self, data):
        data = self.custom_response(data=data, total=1)

        return Response(data=data, status=status.HTTP_200_OK)

    def response_exception_handler(self, response):
        success = status.is_success(response.data['status_code'])
        messages = self.set_errors_exception_handler(response.data)
        data = self.custom_response(success=success, messages=messages)

        return Response(data=data, status=response.data['status_code'])
