from django.contrib import admin
import app.models as models


class IssueAdmin(admin.ModelAdmin):
    empty_value_display = 'N/A'
    list_display = ['title', 'status', 'category', 'owner', 'assignee', 'created_at', 'updated_at']
    list_editable = ['status', 'category', 'assignee']
    list_filter = ['status', 'category', 'owner', 'assignee']
    search_fields = ['title', 'description']

    class Meta:
        model = models.Issue

admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.Status)
admin.site.register(models.Category)
