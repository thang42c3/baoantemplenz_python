from django.db import models
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class ImageLanding(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True, null=True, help_text="You can use HTML tags for styling.")
    image = models.ImageField(upload_to='imagine/')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-imagelanding', args=[self.slug])

    def save(self, *args, **kwargs):
        # Check if any records already exist
        existing_records = ImageLanding.objects.exists()

        if existing_records:
            # Display a message if a record already exists
            message = "A record already exists. Please edit it."
            messages.error(request, message)
        else:
            # If no records exist, save the instance
            super(ImageLanding, self).save(*args, **kwargs)


class Address(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True, null=True, help_text="You can use HTML tags for styling.")
    google_map_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-imagelanding', args=[self.slug])

    def save(self, *args, **kwargs):
        # Check if any records already exist
        existing_records = Address.objects.exists()

        if existing_records:
            # Display a message if a record already exists
            message = "A record already exists. Please edit it."
            messages.error(request, message)
        else:
            # If no records exist, save the instance
            super(Address, self).save(*args, **kwargs)


class SocialMediaLink(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True, null=True, help_text="You can use HTML tags for styling.")
    url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-imagelanding', args=[self.slug])


class Menu(models.Model):
    vn_name = models.CharField(max_length=255)
    vn_slug = models.SlugField(max_length=250)
    en_name = models.CharField(max_length=255)
    en_slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='imagine/', blank=True)

    def __str__(self):
        return self.vn_name

    def get_absolute_vn_url(self):
        return reverse('vn_menu_category', args=[self.vn_slug])

    def get_absolute_en_url(self):
        return reverse('en_menu_category', args=[self.en_slug])


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

