from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("home", views.tasks, name='home'),
    path("about", views.about, name='about'),
    path("France", views.france, name='France'),
    path("Brazil", views.brazil, name='Brazil'),
    path("Portugal", views.portugal, name='Portugal'),
    path("teacher", views.for_teacher, name='for_teacher'),

]

