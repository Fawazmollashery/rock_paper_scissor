from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage for the game
    path('play/', views.play, name='play'),  # Endpoint to handle the game logic
]
