from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def chacolate(request):
    return HttpResponse('naugty guy came with nasty chacooo!!')