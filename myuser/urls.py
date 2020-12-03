from django.urls import include, path
from . import views
from rest_framework import routers
from .views import *
#
# router = routers.DefaultRouter()
# router.register('users', UserViewSet)
#
# urlpatterns = router.urls
urlpatterns = [
    path('', index)
]
