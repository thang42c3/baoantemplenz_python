from django.contrib import admin
# Register your models here.
from django.db import models
from . models import Donation
from ckeditor.widgets import CKEditorWidget


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'vn_slug': ('vn_name',),
        'en_slug': ('en_name',)
    }
    formfield_overrides = {
            models.TextField: {'widget': CKEditorWidget()},
        }
