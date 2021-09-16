from django.urls import path, include
from rest_framework.routers import DefaultRouter

from CustomForms.views import CustomFormViewSet

router = DefaultRouter()
router.register(r'customForms', CustomFormViewSet, 'api_custom_forms')

urlpatterns = [
    path('api/', include(router.urls))
]
