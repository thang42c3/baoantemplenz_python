from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class AboutUsCategory(models.Model):
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    vn_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.vn_name

    def get_absolute_vn_url(self):
        return reverse('vn_aboutuscategories', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_aboutuscategories', args=[self.en_slug])


class AboutUs(models.Model):
    category = models.ForeignKey(AboutUsCategory, related_name='actionsCategory', on_delete=models.SET_NULL, null=True)
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    vn_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='imagine/', blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.vn_name

    def get_absolute_vn_url(self):
        return reverse('aboutus', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('aboutus', args=[self.en_slug])

