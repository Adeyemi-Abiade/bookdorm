from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('rooms/', views.rooms, name="rooms"),
    path('room/<str:pk>', views.room, name="room"),
]