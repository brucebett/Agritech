from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def services(request):
    return render(request, "service.html")

def about(request):
    return render(request, "about.html")