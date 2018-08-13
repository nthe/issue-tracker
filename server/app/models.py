from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=64)


class Status(models.Model):
    title = models.CharField(max_length=64)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    status = models.ForeignKey(
        Status, 
        on_delete=models.CASCADE, 
        null=False, 
        related_name="status")
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        null=False,
        related_name="category"
        )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="owner"
        )
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assignee"
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
