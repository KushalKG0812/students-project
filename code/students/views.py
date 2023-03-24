from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, permissions


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
