from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):
    context = {
        'abc': range(100)
    }
    return render(request, 'ProfileView/index.html', context)
