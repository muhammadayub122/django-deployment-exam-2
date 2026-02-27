from django.urls import path
from .views import StudentListCreateApiView, StudentDetailApiView

urlpatterns = [
    path("student/", StudentListCreateApiView.as_view()),
    path("student/detail/<int:pk>/", StudentDetailApiView.as_view()),
]
