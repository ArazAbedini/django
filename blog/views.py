from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post







class BlogListView(ListView):
    model = Post
    template_name = "blog.html"

class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"