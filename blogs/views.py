from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blogs/allblogs.html', {"blogs":blogs})

def home(request):
    return render(request, 'jobs/home.html')

def details(request,blog_id):
    blogdetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {"blog":blogdetail})