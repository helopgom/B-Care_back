from django.urls import path
from . import views

urlpatterns = [
    path('', views.conversacion_ia, name='conversation_ia'),  # Ruta base para la app
]
