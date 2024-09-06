from django.urls import path
from . import views

urlpatterns = [
    path('conversation/', views.conversacion_ia, name='conversation_ia'),
]
