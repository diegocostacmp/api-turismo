from django.contrib import admin
from .models import Comentario
from .actions import aprova_comentario, reprova_comentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'aprovado']
    actions = [aprova_comentario, reprova_comentario]

admin.site.register(Comentario, ComentarioAdmin)