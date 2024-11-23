from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return render(request, 'main/index.html')

 #def index(request):
    #  return HttpResponse('<h1>Эта страница на разработке<h1>')

# Create your views here.
