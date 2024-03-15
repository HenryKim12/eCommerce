from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    #products = Product.objects.create(name="test")
    return HttpResponse("hello world, this is home")