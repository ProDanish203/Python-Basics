from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.todos, name="todos"),
    path("<int:id>/", views.todo_details, name="todo_details"),
    path("add/", views.add_todo, name="add_todo"),
]
