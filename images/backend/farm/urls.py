# core/urls.py
from django.urls import path
from .views import AuthView

urlpatterns = [
    path('auth/', AuthView.as_view()),  # unified login/signup
]
