from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


class ResponseInfo(object):
    def __init__(self, user=None, **args):
        self.response = {}
        self.response['success'] = args.get('success', True)
        self.response['messages'] = args.get('messages', '')
        self.response['data'] = args.get('data', '')
        self.response['total'] = args.get('total', 1)


class ResponseModelViewSet(viewsets.ModelViewSet):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(ResponseModelViewSet, self).__init__(**kwargs)

    def create(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).create(request, *args, **kwargs)
        self.response_format['data'] = response.data
        data = self.response_format

        return Response(data=data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).retrieve(request, *args, **kwargs)
        self.response_format['data'] = response.data
        data = self.response_format

        return Response(data=data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).update(request, *args, **kwargs)
        self.response_format['data'] = response.data
        data = self.response_format

        return Response(data=data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        response = super(ResponseModelViewSet, self).destroy(request, *args, **kwargs)
        self.response_format['data'] = response.data
        data = self.response_format

        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
