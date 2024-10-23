from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.home, name="home"),
    path("project/", views.project, name="project")
]