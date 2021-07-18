from django.http.response import HttpResponseRedirect
from blog.forms import PostModelForm
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django.shortcuts import render,  redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        if self.request.user != post.author:
            if self.request.user == 'admin':
                return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        if self.request.user != post.author:
            if self.request.user == 'admin':
                return True
        
        return False