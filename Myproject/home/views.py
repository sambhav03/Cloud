from django.shortcuts import render,HttpResponse
def homepage(request):
    return HttpResponse('Welcome')
def aboutpage(request):
    return HttpResponse('Thats about me!')

# Create your views here.
