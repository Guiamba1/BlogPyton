from django.views.generic import DetailView,ListView
from .models import Post
from django.shortcuts import render

# Create your views here.

#classe que vai herdar uma listView
class PostListView(ListView):
    model = Post

#classe que herda DetailView
class PostDetailView(DetailView):
    model = Post