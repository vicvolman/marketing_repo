from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'company', 'email', 'status', 'source', 'estimated_value', 'created_at','is_public_submission']
    list_filter = ['status', 'source', 'created_at', 'is_public_submission']
    search_fields = ['full_name', 'company', 'email', 'phone_number']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = [
        ('Contact Information', {
            'fields': ['full_name', 'company', 'job_title', 'email', 'phone_number']
        }),
        ('Lead Details', {
            'fields': ['source', 'status', 'estimated_value', 'next_follow_up']
        }),
        ('Additional Information', {
            'fields': ['notes']
        }),
        ('System Fields', {
            'fields': ['created_at', 'updated_at', 'is_public_submission', 'public_submission_date'],
            'classes': ['collapse']
        }),
    ]