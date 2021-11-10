from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

# from auto_tests.api.endpoint import ViewSet

router = DefaultRouter()

# router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
