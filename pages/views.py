from django.shortcuts import render
from posts.models import Post
from django.contrib.auth.models import User
import random
# Create your views here.

def home(request):
    lastPosts=Post.objects.all().order_by('-id')[:5] #getting last 3 posts. '-' mean is the last posts. and 3 is display 3 posts
    users=User.objects.filter(groups__name='Yazarlar') #getting users who is in yazarlar group 
    
    randomPosts=Post.objects.all().order_by('?')[:3]

    context={
        'lastposts':lastPosts,
        'users':users,
        'randomPosts':randomPosts,
        
    }
    return render(request,'pages/home.html',context)

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

    