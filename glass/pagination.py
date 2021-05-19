from rest_framework.pagination import PageNumberPagination


class GlassListPagination(PageNumberPagination):
    page_size = 10
