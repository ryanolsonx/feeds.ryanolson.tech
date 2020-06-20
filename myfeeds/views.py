from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    return HttpResponse("Hello, you should later see feed names here.")
