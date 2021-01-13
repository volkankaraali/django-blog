from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *
from django.db.models import Count
from django.core.paginator import Paginator

# Create your views here.

def posts(request):
    posts=Post.objects.all()
    category=Category.objects.order_by('title') #sort as alphabetic
    


    #allow display 5 posts on posts page.  
    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)


    context={
        'posts':posts,
        'category':category,
        
    }
    return render(request,'posts/posts.html',context)

def category(request,category):
    category=Category.objects.get(title=category) #open link as /posts/category/...
    posts=Post.objects.filter(category=category)

    paginator=Paginator(posts,5)
    page=request.GET.get('page')
    posts=paginator.get_page(page)

    context={
        
        'posts':posts,
    }
    
    return render(request,'posts/category.html',context)

def detail(request,title):
    post=get_object_or_404(Post,title=title)
    #post=Post.objects.get(id=pk)
    context={
        'post':post,
    }
    return render(request,'posts/detail.html',context)


