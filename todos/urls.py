from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDestroyView

urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
]
