from django.contrib import admin
# Register your models here.
from django.db import models
from . models import ImageGallery, MediaGallery, GalleryCategories
from ckeditor.widgets import CKEditorWidget


@admin.register(GalleryCategories)
class GalleryCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'vn_slug': ('vn_name',),
        'en_slug': ('en_name',)
    }
    formfield_overrides = {
            models.TextField: {'widget': CKEditorWidget()},
        }
    list_display = ('vn_name', 'en_name')  # Fields to display in the list view
    search_fields = ('vn_name', 'en_name')  # Fields to search by in the list view


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'vn_slug': ('vn_name',),
        'en_slug': ('en_name',)
    }
    formfield_overrides = {
            models.TextField: {'widget': CKEditorWidget()},
        }
    list_display = ('en_name', 'vn_name')  # Fields to display in the list view
    search_fields = ('en_name', 'vn_name',)  # Fields to search by in the list view


@admin.register(MediaGallery)
class MediaGalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'vn_slug': ('vn_name',),
        'en_slug': ('en_name',)
    }
    formfield_overrides = {
            models.TextField: {'widget': CKEditorWidget()},
        }
    list_display = ('en_name', 'vn_name')  # Fields to display in the list view
    search_fields = ('en_name', 'vn_name',)  # Fields to search by in the list view
