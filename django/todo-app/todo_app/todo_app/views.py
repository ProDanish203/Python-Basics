from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     # return HttpResponse("Hello, Django!")
#     return render(request, "index.html")


def about(request):
    return HttpResponse("Hello, About from Django!")


def contact(request):
    return HttpResponse("Hello, Contact from Django!")
