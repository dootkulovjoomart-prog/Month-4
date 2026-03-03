from django.shortcuts import render
from .models import Celebrities

# Create your views here.

def celebrity_list(request):
    celebrities = Celebrities.objects.all()
    return render(request , 'main/index.html',{'celebrities' : celebrities })


def look_detail(request , id ):
    detail = Celebrities.objects.get(id=id)
    return render(request , 'main/detail_look.html' ,  {'celebrities' : detail })   

def nav_bar(request):
    return render(request , 'main/home.html' )