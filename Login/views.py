from Blog import settings
import os
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .mode import *
from board.forms import CommentForm


from .models import Post, PostComment

def HomePage(request):
    posts = Post.objects.all()
    recents = Post.objects.all().order_by('created_at').first()
    if DARK_MODE:
        MODE = True
    else:
        MODE = False
    return render(request, 'home.html', {"posts":posts,"recents":recents,"dark":MODE})

def LoginPage(request):
    if request.method == "POST":
        username = request.POST["identifiant"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect(HomePage)
        else:
            messages.info(request, "Authentification error")
            posts = Post.objects.all()
            return redirect(LoginPage)
    
    if DARK_MODE:
        MODE = True
    else:
        MODE = False
    return render(request, 'login.html', {"dark":MODE})

def RegisterPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["pwsd"]
        new_user = User.objects.create_user(username, email, password)
        new_user.save()

        return redirect(LoginPage)
    if DARK_MODE:
        MODE = True
    else:
        MODE = False
    return render(request, 'register.html', {"dark":MODE})

def LogoutPage(request):
    logout(request)
    return redirect(HomePage)

def postPage(request, pk):
    post = Post.objects.get(pk=pk)
    recents = Post.objects.all().order_by('created_at').first()
    
    if request.method == "POST":
        cmt_forms = CommentForm(request.POST)
        if cmt_forms.is_valid():
            cmt = cmt_forms.save(commit=False)
            cmt.editor = request.user
            cmt.post = post
            cmt.save()
    else:
        cmt_forms = CommentForm()

    if DARK_MODE:
        MODE = True
    else:
        MODE = False
    return render(request, 'Posts.html', {
        "post":post,
        "recents":recents,
        "dark":MODE,
        "cmtForm":cmt_forms
        })

@csrf_exempt
def darkMode(request):
    if request.method == 'POST':
        base = os.path.dirname(__file__)
        file_path = os.path.join(base, 'mode.py')
        with open(file_path, 'w') as fs:
            if DARK_MODE:
                fs.write('LIGHT_MODE = True \n')
                fs.write('DARK_MODE = False')
            else:
                fs.write('LIGHT_MODE = False \n')
                fs.write('DARK_MODE = True')
            
    return JsonResponse({})
    #pass
