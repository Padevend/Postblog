from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from Login.views import HomePage, LoginPage
from Login.mode import *
from Login.models import Post
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='login')
def overview(request):
    if DARK_MODE:
        MODE = True
    else:
        MODE = False
        
    user_post = Post.objects.filter(author=request.user)
    total_post = user_post.__len__()

    return render(request, 'Posts/post_admin.html', {
        "dark":MODE,
        "userPost":user_post,
        "totalPost":total_post
        })

def deletePost(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect(overview)

def editPost(request, post_id):
    if DARK_MODE:
        MODE = True
    else:
        MODE = False
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        forms = PostForm(request.POST, request.FILES, instance=post)
        if forms.is_valid():
            forms.save()
            return redirect(overview)
    else:
        forms = PostForm(instance=post)

    return render(request, "Posts/add_post.html", {
        "Forms":forms,
        "dark":MODE,
    })

def addPost(request):
    if DARK_MODE:
        MODE = True
    else:
        MODE = False
    if request.method == "POST":
        forms = PostForm(request.POST, request.FILES)
        if forms.is_valid():
            blog = forms.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect(overview)
    else:
        forms = PostForm()

    return render(request, "Posts/add_post.html", {
        "Forms":forms,
        "dark":MODE,
    })

def commentView(request):
    if DARK_MODE:
        MODE = True
    else:
        MODE = False
    
    posts = Post.objects.filter(author=request.user)
    total = 0
    for post in posts:
        for i in post.comments.all():
            total += 1

    return render(request, "Posts/comments.html", {
        "dark":MODE,
        "posts":posts,
        "totalComment":total
    })