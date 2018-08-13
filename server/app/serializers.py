from rest_framework import serializers
import app.models as models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Issue
        fields = '__all__'
