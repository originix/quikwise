from .pagination import PageNumberPagination
from django.conf import settings


class MaxPagination(PageNumberPagination):
    page_size = settings.API_MAX_PAGE_SIZE
