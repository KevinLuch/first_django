from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("kevin", views.kevin, name="kevin"),
    path("yeezy", views.yeezy, name="yeezy")
]