from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_form),
    path('register_real/', views.register_real),
]
