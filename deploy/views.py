from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Student
from .serializer import  StudentSerializer
from rest_framework.pagination import PageNumberPagination
class Custompaginator(PageNumberPagination):
    page_size=20

from rest_framework.permissions import  AllowAny
# Create your views here.
class StudentListCreateApiView(ListCreateAPIView):
    queryset=Student
    serializer_class=StudentSerializer
    permission_classes=[AllowAny]
    pagination_class = Custompaginator


class StudentDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]