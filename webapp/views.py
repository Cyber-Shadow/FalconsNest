from django.shortcuts import render


def index(request):
    return render(request, "webapp/home.html")


def login(request):
    return render(request, "webapp/login.html")
