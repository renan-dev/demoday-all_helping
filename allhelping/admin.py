from django.contrib import admin
from .models import Ajudado, Ajudante, Match, Mensagem

# Register your models here.

admin.site.register(Ajudado)
admin.site.register(Ajudante)
admin.site.register(Match)
admin.site.register(Mensagem)