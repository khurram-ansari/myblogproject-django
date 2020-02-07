from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Categories
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

all_cat=Categories.objects.all()
def allblogs(request):
    blog=Blog.objects.all().order_by('created_at')
    return render(request,'index-content.html',{"categories":all_cat,"blog":blog})

def getsingleblog(request,slug):    
    single_blog=Blog.objects.get(slug=slug)
    return render(request,'single-blog-content.html',{"categories":all_cat,"singleblog":single_blog})

@login_required(login_url='/accounts/login')
def create_blog(request):
    if request.method=='POST':
        form=forms.CreateBlog(request.POST,request.FILES)
        if form.is_valid():
            #save blogs to db
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            return redirect('blog:allblogs')

    else:
        form=forms.CreateBlog()
        return render(request,'blog_create.html',{'categories':all_cat,'creationform':form})

def getcatblog(request,cat):
    cat_id=Categories.objects.get(name=cat)
    cat_blog=Blog.objects.all().filter(category_id=cat_id)
    # return HttpResponse(cat.id)
    return render(request,'category_blog.html',{"categories":all_cat,"catblog":cat_blog,"catname":cat})