from django.shortcuts import render, redirect 
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from listings.forms import ContactUsForm, BandForm
from django.core.mail import send_mail

# Create your views here.

def hello(request):
    
    bands = Band.objects.all()

    return render(request, 'listings/hello.html', {'bands': bands, 'page_name': "Hello"})

def band_list(request):
    bands = Band.objects.all()

    return render(request,'listings/band_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)

    return render(request, 'listings/band_detail.html', context={'band': band})


def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    listings = Listing.objects.all()

    return render(request, 'listings/listings.html', context={'listings': listings})

def contact(request):

    form = ContactUsForm()

    print('la methode de requete est :', request.method)
    print("Les données POST sont : ", request.POST)

    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via merche Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-send')
    else:
        form = ContactUsForm()
        
    return render(request, 'listings/contact.html', context={'form': form})

def home(request):
    return render(request, 'listings/home.html')

def email_send(request):
    return render(request, 'listings/email_send.html')


def band_create(request):
    
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})