from django.urls import path
from .views import ProfileListCreateView, ProfileDetailView

urlpatterns = [
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail')
]
