from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import NewsSerializer
from .models import NewsModel
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import StaffPermissionClass, AdminPermissionClass



class CreateView(generics.CreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, StaffPermissionClass)


class AllApiView(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return NewsModel.objects.filter(status=True)


class UpdateStatus(generics.UpdateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, AdminPermissionClass)