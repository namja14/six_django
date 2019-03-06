from allauth.socialaccount.models import SocialApp
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Blog # 이거써서 가져오기
from blog.models import Portfolio
# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Portfolio()
    blog.title = request.GET['title']
    blog.image = request.GET['image']
    blog.description = request.GET['description']
    blog.save()
    return redirect('')
    

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> post  
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
        else:
            return render(request, 'photo.html', {'portfolios':portfolios})
    #2. 빈 페이지를 띄어주는 기능 -> get
    else:
        form = BlogPost()
        return render(request,'new.html',{'form':form})
        