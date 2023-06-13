from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing

# Create your views here.

def hello(request):
    
    bands = Band.objects.all()

    return render(request, 'listings/hello.html', {'bands': bands, 'page_name': "Hello"})

def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    listings = Listing.objects.all()

    return render(request, 'listings/listings.html', context={'listings': listings})

def contact(request):
    return render(request, 'listings/contact.html')

def home(request):
    return render(request, 'listings/home.html')