from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import *

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-name')
    mvps = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvps': mvps,
    }
    return render(request, 'pages/about.html', context)