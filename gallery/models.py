from django.db import models
from django.utils import timezone
from django.urls import reverse


class GalleryCategories(models.Model):
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    vn_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.vn_name

    def get_absolute_vn_url(self):
        return reverse('vn_categories', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_categories', args=[self.en_slug])


# Create your models here.
class ImageGallery(models.Model):
    category = models.ForeignKey(GalleryCategories, related_name='imagegallery', on_delete=models.SET_NULL, null=True)
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
        return reverse('vn_img_gallery', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_img_gallery', args=[self.en_slug])


class MediaGallery(models.Model):
    category = models.ForeignKey(GalleryCategories, related_name='mediagallery', on_delete=models.SET_NULL, null=True)
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    vn_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)
    ulr = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.vn_name

    def get_absolute_vn_url(self):
        return reverse('vn_media_gallery', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_media_gallery', args=[self.en_slug])
