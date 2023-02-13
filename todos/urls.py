from rest_framework import routers
from .views import Todo

router = routers.DefaultRouter()
router.register('todo', TodoViewset)

from django.urls import path
from profiles import views

urlpatterns = [
    path('todo/', views.Todo.as_view()),
    path('todo/<int:pk>/', views.ToDoDetail.as_view())
]