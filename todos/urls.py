from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo-detail'),
#    path('projects/', ProjectList.as_view(), name='project-list-create'),
#    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]
