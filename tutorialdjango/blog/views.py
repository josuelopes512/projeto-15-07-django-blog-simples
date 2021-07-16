from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post



