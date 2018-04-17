from django.http import HttpResponse
import time

def hello(request):
    return HttpResponse("Hello world!This is my first demo")

def current_time(request):
    return HttpResponse(time.strftime('%Y-%m-%D %H-%M-%S'))