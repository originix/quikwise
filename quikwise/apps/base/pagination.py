from apps.base.response import Response
from collections import OrderedDict
from django.conf import settings
from rest_framework.pagination import PageNumberPagination as BasePageNumberPagination
from rest_framework import status


class PageNumberPagination(BasePageNumberPagination):
    """
    A json-api compatible pagination format
    """

    page_size_query_param = settings.API_PAGINATE_BY_PARAM
    max_page_size = settings.API_MAX_PAGE_SIZE
    page_size = settings.API_PAGE_SIZE

    def get_paginated_response(self, data):

        meta = OrderedDict([
            ('page', self.page.number),
            ('pages', self.page.paginator.num_pages),
            ('page_size', self.page_size),
            ('total', self.page.paginator.count),
        ])

        return Response(data=data, meta=meta, status=status.HTTP_200_OK)

class MaxPagination(PageNumberPagination):
    page_size = settings.API_MAX_PAGE_SIZE
