from django.urls import path,include
from rest_framework import routers
from .views import FollowedCryptoViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('followed', FollowedCryptoViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]