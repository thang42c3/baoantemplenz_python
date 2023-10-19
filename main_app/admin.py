from django.contrib import admin
# Register your models here.
from django.db import models
from . models import ImageLanding, Menu, ContactMessage
from ckeditor.widgets import CKEditorWidget

@admin.register(ImageLanding)
class ImageLandingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'image', 'created_at')  # Fields to display in the list view
    list_filter = ('created_at',)  # Fields to filter by in the list view
    search_fields = ('name',)  # Fields to search by in the list view
    date_hierarchy = 'created_at'  # Add a date-based drilldown navigation by 'created_at'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'vn_slug': ('vn_name',),
        'en_slug': ('en_name',)
    }
    formfield_overrides = {
            models.TextField: {'widget': CKEditorWidget()},
        }
    list_display = ('en_name', 'vn_name')  # Fields to display in the list view
    search_fields = ('en_name', 'vn_name',)  # Fields to search by in the list view


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'name': ('name',),
        'subject': ('subject',)
    }
    list_display = ('name', 'subject', 'email')  # Fields to display in the list view
    search_fields = ('name', 'subject', 'email')  # Fields to search by in the list view

