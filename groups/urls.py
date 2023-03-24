from django.urls import path
from .views import GroupList, GroupDetail

urlpatterns = [
    path('groups/', GroupList.as_view(), name="group-list"),
    path('groups/<int:pk>/', GroupDetail.as_view(), name="group-detail")
]