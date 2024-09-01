from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet
from .views import UserProfileCreateView

router = DefaultRouter()
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-profile/', UserProfileCreateView.as_view(), name='user-profile-create'),
]
