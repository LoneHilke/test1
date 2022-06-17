import os
from django.shortcuts import render
from django.http import JsonResponse
#import request


def home(request):
    return render(request, 'index.html')

def hilsen(request):
    return render(request, 'hilsen.html')
  
def info(request):
    return render(request, 'info.html')
