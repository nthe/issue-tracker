from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.title


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
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Issue'
        verbose_name_plural = 'Issues'

    def __str__(self):
        return self.title
