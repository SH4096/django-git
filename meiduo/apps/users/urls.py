from django.contrib import admin
from django.urls import path
from apps.users import views

urlpatterns = [
    path('usernames/<username:username>/count', views.UsernameCountView.as_view()),
]
