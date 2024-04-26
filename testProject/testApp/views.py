from django.shortcuts import render
from .models import Blog
from .forms import BlogPost
from django.utils import timezone

# Create your views here.
def home(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
    else:
        form = BlogPost()
    blogs = Blog.objects
    return render(request,'home.html', {'form':form, 'blogs':blogs})  # html 파일(template)을 연결