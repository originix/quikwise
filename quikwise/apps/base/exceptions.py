from apps.base.response import Response
from rest_framework.views import exception_handler as base_exception_handler

def get_error_description(error):
    if type(error) == list:
        return [e.title() for e in error]

    return [error.title()]

def get_error_code(error):

    if type(error) == list:
        return " ".join([e.code for e in error])

    return error.code

def format_errors(messages):
    return ' '.join(messages[:2]) + (f" and more (+{len(messages) - 2})" if len(messages) > 2 else '')

def set_errors_exception_handler(e):
    exceptions = e.copy()
    errors = []
    descriptions = []

    for exception in exceptions:
        code = get_error_code(exceptions[exception])
        description = get_error_description(exceptions[exception])

        descriptions.extend(description)

        errors.append({'ref': exception, 'code': code, 'desc': description})

    errors_text = format_errors(descriptions)

    return errors_text, errors

def exception_handler(exc, context):
    response = base_exception_handler(exc, context)

    if response:
        messages, errors = set_errors_exception_handler(response.data)

        return Response(status=response.status_code, message=messages, errors=errors)


class Error(Exception):
    pass

