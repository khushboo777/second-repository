from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<marquee><h1> hello world This is my first string <marquee></h1>')

def first_htmlpage(request):
    return render(request,'first_htmlpage.html')
