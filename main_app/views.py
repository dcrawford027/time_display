from django.shortcuts import render
from time import gmtime, localtime, strftime
from django.utils import timezone

# Create your views here.
def index(response):
    context = {
        'time': timezone.now()
    }
    return render(response, 'index.html', context)