from django.shortcuts import render
from rest_framework import generics
import app.serializers as serializers
import app.models as models


class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = (IsStaffUser,)


class CategoryCreateEditView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # permission_classes = (IsSuperUser,)


class StatusListView(generics.ListAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    # permission_classes = (IsStaffUser,)


class StatusCreateEditView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    # permission_classes = (IsSuperUser,)


class IssueListView(generics.ListAPIView):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    # permission_classes = (IsStaffUser,)


class IssueCreateEditView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = models.Issue.objects.all()
    serializer_class = serializers.IssueSerializer
    # permission_classes = (IsSuperUser,)
