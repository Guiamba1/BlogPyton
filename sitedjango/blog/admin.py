from django.contrib import admin
from django.contrib.auth import models
from .models import Post

# Register your models here.
#Registre seus modelos aqui.

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo","slug","autor","criadoEm","actualizadoEm")
    autoPreencher = {"slug":("titulo",)}