from multiprocessing import AuthenticationError
from django.shortcuts import render
from .serializers import studentSerializer
from rest_framework import viewsets
from .models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser , AllowAny
# from permission.api import serializers
# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    #Quyen nay chi cho phep nguoi dung da xac thuc hoac da dang nhap truy cap API
    # permission_classes = [IsAuthenticated]
    # Quyen nay khong han che nguoi dung truy cap
    # permission_classes = [AllowAny]
    #Quyen nay chir cho phep nguoi quan tri user.staff = True
    permission_classes = [IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = studentSerializer
   