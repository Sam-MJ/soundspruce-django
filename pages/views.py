from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "pages/index.html")


def about(request):
    title = "About"
    context = {"title": title}
    return render(request, "pages/about.html", context)


def products():
    return


def contact():
    return


def articles():
    return
