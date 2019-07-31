from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    my_title = "Hello there...."
    context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "hello_world.html", {"title": "About"})


def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact Us"})
