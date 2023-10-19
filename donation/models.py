from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Donation(models.Model):
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    vn_description = models.TextField(blank=True, null=True)
    en_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.vn_name

    def get_absolute_vn_url(self):
        return reverse('vn_actionscategories', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_actionscategories', args=[self.en_slug])
