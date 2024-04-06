from django.contrib import admin
from .models import BugReport, FeatureRequest

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'task', 'project', 'priority')
    list_editable = ('status',)
    search_fields = ('title', 'description')
    fieldsets = [
        (
            None,
            {
                'fields': ['project', 'title', 'description', 'task']
            }
        ),
        (
            'Advanced Options',
            {'fields': ['status', 'priority']}
        )
    ]

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'created_at', 'updated_at', 'priority')
    list_filter = ('status', 'task', 'project', 'priority')
    search_fields = ('title', 'description')
    fieldsets = [
        (
            None,
            {
                'fields': ['project', 'title', 'description', 'task']
            }
        ),
        (
            'Advanced Options',
            {'fields': ['status', 'priority']}
        )
    ]
