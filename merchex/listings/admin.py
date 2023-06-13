from django.contrib import admin

# Register your models here.

from listings.models import Band
from listings.models import Listing

## ModelAdmin permettent de configurer la manière dont les objets du modèle sont affichés dans l'administration

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed','genre') ### liste des champs que l'on souhaite sur l'affichage de la liste

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year')


#admin.site.register(Band)
#admin.site.register(Listing)

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)