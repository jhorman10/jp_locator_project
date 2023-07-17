from django.urls import path
from . import views

urlpatterns = [
    path('localizacion/', views.obtener_ubicacion_y_mensaje, name='obtener_ubicacion_y_mensaje'),
]