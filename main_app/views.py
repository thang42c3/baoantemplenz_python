from django.shortcuts import render, redirect
from .models import ImageLanding, Menu, ContactMessage
from gallery.models import GalleryCategories, ImageGallery, MediaGallery
from action.models import ActionsCategory, Action
from aboutus.models import AboutUsCategory, AboutUs
from django.core.paginator import Paginator
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def index(request):
    imagelanding = ImageLanding.objects.latest('created_at')
    image_gallery_list = ImageGallery.objects.all().order_by('created_at')
    paginator = Paginator(image_gallery_list, 6)
    page = request.GET.get('page')
    image_galleries = paginator.get_page(page)

    media_galleries = MediaGallery.objects.all()
    gallery_categories = GalleryCategories.objects.all()

    context = {
        'imagelanding': imagelanding,
        'image_galleries': image_galleries,
        'media_galleries': media_galleries,
        'gallery_categories': gallery_categories,
    }

    return render(request, 'main_app/index.html', context=context)


def menu_views(request):
    about_us = Menu.objects.filter(en_slug='about-us').first()
    action = Menu.objects.filter(en_slug='action').first()
    gallery_categories = GalleryCategories.objects.all()
    action_categories = ActionsCategory.objects.all()[:4]
    aboutus_categories = AboutUs.objects.all()

    about_us_detail = AboutUs.objects.filter(en_slug='about-us').first()
    history = AboutUs.objects.filter(en_slug='history').first()
    abbot = AboutUs.objects.filter(en_slug='abbot').first()
    policy = AboutUs.objects.filter(en_slug='policy').first()

    # Create a list of dictionaries where each dictionary represents a menu and its associated submenus
    context = {
        'about_us': about_us,
        'action': action,
        'gallery_categories': gallery_categories,
        'action_categories': action_categories,
        'aboutus_categories': aboutus_categories,
        'about_us_detail':about_us_detail,
        'history':history,
        'abbot':abbot,
        'policy':policy

    }
    return context


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # Create and save a ContactMessage object
        contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact_message.save()
        return render(request, 'main_app/success.html')
    return redirect('index')

