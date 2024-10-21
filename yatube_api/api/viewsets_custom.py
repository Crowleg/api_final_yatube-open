from rest_framework import mixins, viewsets


class BaseGetPostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    '''Кастомная реализация базового viewset для GET и POST'''
