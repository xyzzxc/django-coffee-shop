from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from coffees.models import Coffee


def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', {'coffees': coffees})
