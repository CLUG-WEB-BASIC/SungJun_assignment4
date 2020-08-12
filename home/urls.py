from django.urls import path
from . import views

#.은 myapp

urlpatterns = [
    path('', views.home, name = 'home'),
]