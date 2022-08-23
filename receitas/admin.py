from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria') #mostra no admin 
    list_display_links = ('id', 'nome_receita')
    search_fields = ['nome_receita',]
    list_filter = ('categoria',)

admin.site.register(Receita, ListandoReceitas) #tem que passar aqui a classe do que voce quer mostrar no admin
