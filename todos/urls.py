from django.urls import path
from .views import TodoList, TodoDetail

urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
#    path('projects/', ProjectList.as_view(), name='project-list-create'),
#    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]
