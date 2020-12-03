from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create_task", views.create_task, name="create task"),
    path("get_tasks", views.get_all_tasks, name="get all tasks"),
    path("delete_tasks", views.delete_all_tasks, name="delete all tasks"),
]
