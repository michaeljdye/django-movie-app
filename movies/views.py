from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'movies': ['The Matrix', 'Lord of the Rings', 'Couples Retreat']
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')