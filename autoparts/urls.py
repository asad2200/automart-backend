from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemList


router = DefaultRouter()

router.register('items', ItemList, 'item-detail')

urlpatterns = [
    path('', include(router.urls))
]
