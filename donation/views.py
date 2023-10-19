from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from . models import Donation
# Create your views here.


def donation(request):
    donation_obj  = Donation.objects.first()
    return render(request, 'donation.html', {'donation': donation_obj})
