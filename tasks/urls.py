from django.urls import path
from .views import tasks_list, task_detail, task_create, task_update, task_delete

app_name = 'tasks'

urlpatterns = [
    path('', tasks_list, name='task-list'),
    path('<int:pk>/', task_detail, name='task-detail'),
    path('<int:pk>/update', task_update, name='task-update'),
    path('<int:pk>/delete', task_delete, name='task-delete'),
    path('create/', task_create, name='task-create')
]
