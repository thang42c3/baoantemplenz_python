from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from . models import AboutUs
# Create your views here.


def single_aboutus_post(request, en_slug=None):
    single_post = AboutUs.objects.filter(en_slug=en_slug).first()
    return render(request, 'aboutus_post.html', {'single_post': single_post})