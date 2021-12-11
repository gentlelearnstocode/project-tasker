from django.urls import path
from .views import TaskCreateView, TaskDetailView, TaskDeleteView, TaskListView, TaskUpdateView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('create/', TaskCreateView.as_view(), name='task-create')
]
