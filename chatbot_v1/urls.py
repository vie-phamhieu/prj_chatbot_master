from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("get", views.get_bot_response, name="get_bot_response"),
]