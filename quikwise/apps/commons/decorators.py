from functools import wraps
from .errors import Error


def check_in_attributes(attr_names):
    """
    check if the wrapped function's class have the specified attributes
    :param attr_names: array of attribute names to check
    :return:
    """
    def layer(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            for attr in attr_names:
                if getattr(self, attr, None) is None:
                    error_message = "'{0}' should include a '{1}' attribute".format(self.__class__.__name__, attr)

                    raise Error(error_message)
            return func(self, *args, **kwargs)
        return wrapper
    return layer
