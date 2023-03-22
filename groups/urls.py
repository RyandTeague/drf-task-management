from django.urls import path
from groups import views

urlpatterns = [
    path('groups/', views.GroupList.as_view(), name="group-list"),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name="group-detail")
]