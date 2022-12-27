from django.contrib import admin

from . import models

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(models.Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    pass

@admin.register(models.FeedbackRequest)
class FeedbackRequestAdmin(admin.ModelAdmin):
    list_display = ('email', 'website')

@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('contact_number', 'contact_number_wa', 'address', 'email')