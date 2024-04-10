from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('call-flask-api/', views.call_flask_api, name='call_flask_api'),
]