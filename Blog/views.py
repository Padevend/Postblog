from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def HomePage(request):
    return render(request, 'home.html')

def LoginPage(request):
    return render(request, 'login.html')

def RegisterPage(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["pwsd"]
        return redirect('HomePage')
    else:
        messages.error(request, "Un probleme a été rencontrer lors de la creation du compte")
    return render(request, 'login.html')