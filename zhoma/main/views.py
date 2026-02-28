from django.shortcuts import render
from .models import Celebrities

# Create your views here.

def celebrity_list(request):
    celebrities = Celebrities.objects.all()
    return render(request , 'main/index.html',{'celebrities' : celebrities })


