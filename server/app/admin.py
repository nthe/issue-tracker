from django.contrib import admin
from django.db.models import F, ExpressionWrapper, fields, Avg, Max, Min
from django.urls import path
import app.models as models


def tdToDHM(td):
    return {
        'days': td.days,
        'hours': td.seconds//3600,
        'seconds': (td.seconds//60)%60
    }


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
        if extra_context is None:
            extra_context = {}
        extra_context['title'] = 'Issue Tracker'
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data["cl"].queryset
        except (AttributeError, KeyError):
            return response
        
        # prepare database expression
        resolution_time = ExpressionWrapper(F('updated_at') - F('created_at'), output_field=fields.DurationField())

        # make sure we're calculating using only closed issues
        f_qs = qs.filter(status__title__iexact='closed')
        f_qs = f_qs.annotate(resolution_time=resolution_time)
        maximum = f_qs.aggregate(Max('resolution_time'))['resolution_time__max']
        minimum = f_qs.aggregate(Min('resolution_time'))['resolution_time__min']
        average = f_qs.aggregate(Avg('resolution_time'))['resolution_time__avg']
        
        metrics = {
            'minimum': tdToDHM(minimum),
            'maximum': tdToDHM(maximum),
            'average': tdToDHM(average),
            'closed': f_qs.count(),
            'total': qs.count()
        }

        response.context_data['metrics'] = metrics
        return response

admin.site.register(models.Issue, IssueAdmin)
admin.site.register(models.Status)
admin.site.register(models.Category)

admin.site.site_header = "Issue Tracker"
admin.site.site_title = "Issue Tracker Portal"
admin.site.index_title = "Welcome to Issue Tracker Portal"