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
        # Check if the instance has a primary key (i.e., it's being edited)
        if self.pk:
            super(ImageLanding, self).save(*args, **kwargs)
        else:
            # Display a message or raise an exception to prevent adding new data
            pass



class ContactInformation(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    google_map_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    email=models.TextField(blank=True, null=True)
    phone=models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact_information', args=[self.slug])

    def save(self, *args, **kwargs):
        # Check if the instance has a primary key (i.e., it's being edited)
        if self.pk:
            super(ContactInformation, self).save(*args, **kwargs)
        else:
            # Display a message or raise an exception to prevent adding new data
            pass


class SocialMediaLink(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    url_twitter = models.TextField(blank=True, null=True)
    url_facebook = models.TextField(blank=True, null=True)
    url_instagram = models.TextField(blank=True, null=True)
    url_google_plus = models.TextField(blank=True, null=True)
    url_linkedin = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list-social-media', args=[self.slug])

    def save(self, *args, **kwargs):
        # Check if the instance has a primary key (i.e., it's being edited)
        if self.pk:
            super(SocialMediaLink, self).save(*args, **kwargs)
        else:
            # Display a message or raise an exception to prevent adding new data
            pass


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

