from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def biriyani(request):
    return HttpResponse('Spicy chicken biriyaniiii')

def icecream(request):
    return HttpResponse('cool chocolate icecreammmm')