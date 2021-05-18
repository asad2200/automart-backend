from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyList, CarList, GlassList, ModelList

router = DefaultRouter()

router.register('companys', CompanyList)
router.register('cars', CarList)
router.register('models', ModelList)
router.register('glass-list', GlassList)

urlpatterns = [
    path("", include(router.urls))
]
