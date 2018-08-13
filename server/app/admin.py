from django.contrib import admin
from django.db.models import F, ExpressionWrapper, fields, Avg, Max, Min
from django.urls import path
import app.models as models



class IssueAdmin(admin.ModelAdmin):
    change_list_template = 'stats.html'
    empty_value_display = 'N/A'
    list_display = ['title', 'status', 'category', 'owner', 'assignee', 'created_at', 'updated_at']
    list_editable = ['status', 'category', 'assignee']
    list_filter = ['status', 'category', 'owner', 'assignee']
    search_fields = ['title', 'description']
    ordering = ['-updated_at']

    class Meta:
        model = models.Issue

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response
        
        f_qs = qs.filter(status__title__iexact='open')

        resolution_time = ExpressionWrapper(F('updated_at') - F('created_at'), output_field=fields.DurationField())
        f_qs = f_qs.annotate(resolution_time=resolution_time)
        maximum = f_qs.aggregate(Max('resolution_time'))['resolution_time__max']
        minimum = f_qs.aggregate(Min('resolution_time'))['resolution_time__min']
        average = f_qs.aggregate(Avg('resolution_time'))['resolution_time__avg']
        
        metrics = {
            'minimum': repr(minimum),
            'maximum': repr(maximum),
            'average': repr(average)
        }

        response.context_data['metrics'] = metrics
        return response

admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.Status)
admin.site.register(models.Category)
