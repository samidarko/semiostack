from django.contrib import admin
from models import Semiocoder


class SemiocoderAdmin(admin.ModelAdmin):
    """Classe d'administration de l'objet Joblist
    """
    list_display = ( 'name', 'adresse', )
    search_fields = ('name', 'adresse', )

admin.site.register(Semiocoder, SemiocoderAdmin)
