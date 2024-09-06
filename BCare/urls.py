from django.contrib import admin
from django.urls import path, include
BASE_URL = 'api/v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include('users.urls')),
    path(f'{BASE_URL}conversation/', include('conversation.urls')),
]
