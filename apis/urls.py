from django.urls import path, include
from . import views
from .views.v1.todolist import taskList, taskDetail,taskCreate, taskUpdate, taskDelete

urlpatterns = [
    path('todo-list/', taskList, name='todo-list'),
    path('task-detail/<str:pk>', taskDetail, name='task-detail'),
    path('task-create/', taskCreate, name='task-create'),
    path('task-updates/<str:pk>', taskUpdate, name='task-updates'),
    path('task-delete/<str:pk>', taskDelete, name='task-delete'),
]