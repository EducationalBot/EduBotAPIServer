from django.conf import settings
from django.conf.urls import url
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
# from auto_tests.api.endpoint import UserViewSet

# from auto_tests import urls as auto_tests_url

# user_router = DefaultRouter()
# user_router.register(r'users', UserViewSet)


api_endpoint_view = [
    # url(r'', include(user_router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_endpoint_view)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

