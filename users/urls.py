from django.urls import path
from .views import UserProfileViewSet, UserLoginView, UserDetailView, UserUpdateView


urlpatterns = [
    path('profile/', UserProfileViewSet.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('profile/update/', UserUpdateView.as_view(), name='user_update')
]