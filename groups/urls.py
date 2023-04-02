from django.urls import path
from .views import GroupListCreateAPIView, GroupRetrieveUpdateDestroyAPIView, UserListAPIView


urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view(), name="group-list"),
    path('groups/<int:pk>/', GroupRetrieveUpdateDestroyAPIView.as_view(), name="group-detail"),

    path('users/', UserListAPIView.as_view(), name="user-list"),
]