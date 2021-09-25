from django.contrib.auth.models import User
from django.db import models as md
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.
# Crie seus modelos aqui

class Post(md.Model):
    titulo =  md.CharField(max_length=255)
    slug = md.SlugField(max_length=255, unique=True)
    autor = md.ForeignKey(User,on_delete=md.CASCADE)
    messagem = md.TextField()
    criadoEm = md.DateTimeField(auto_now_add=True)
    actualizadoEm = md.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-criadoEm"),

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    
