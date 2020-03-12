from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/aboutus.html')


def menu(request):
    return render(request, 'blog/menu.html')


def contact(request):
    return render(request, 'blog/contact.html')


