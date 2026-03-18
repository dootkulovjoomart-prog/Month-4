from django.shortcuts import render , redirect
from .models import Celebrities , Trophy, Club
from .form import CreateCelebrities , SearchForm
from django.http import HttpResponse
from django.db.models import Q
import math
# Create your views here.

def celebrity_list(request):
    if request.method == "GET":
        all_celebrities = Celebrities.objects.all()
        form = SearchForm(request.GET)
        if not form.is_valid():
            return HttpResponse("Error")
        search = form.cleaned_data.get("search", None)
        club = form.cleaned_data.get("club", None)
        trophy = form.cleaned_data.get("trophy", None)
        if search :
            all_celebrities = all_celebrities.filter(Q(name__icontains = search))
        if club:
            all_celebrities = all_celebrities.filter(club=club)
        if trophy:
            all_celebrities = all_celebrities.filter(trophy__in=trophy)
        limit = 3
        page = int(request.GET.get("page", 1))
        max_page =math.ceil(all_celebrities.count() / limit )
        list_pages = range(1 , max_page +1 )
        start = (page -1)* limit
        end = page * limit 
        all_celebrities = all_celebrities[start:end]
        return render(request , 'main/index.html',{'celebrities' : all_celebrities, "form" : form , "list_pages":list_pages})


def look_detail(request , id ):
    if request.method == "GET":
        detail = Celebrities.objects.get(id=id)
        return render(request , 'main/detail_look.html' ,  {'celebrities' : detail })   

def nav_bar(request):
    if request.method == "GET":
        return render(request , 'main/home.html' )

def create_celebrities(request):
    if request.method == "POST":
        name = request.POST.get("name")
        image = request.FILES.get("image")
        profession = request.POST.get("profession")
        discription = request.POST.get("discription")
        content = request.POST.get("content")
        date = request.POST.get("date")
        club_id = request.POST.get("club")
        trophy_ids = request.POST.getlist("trophy")  

        club = Club.objects.get(id=club_id) if club_id else None
      
        celebrity = Celebrities.objects.create(
            name=name,
            image=image,
            profession=profession,
            discription=discription,
            content=content,
            date=date,
            club=club,
            
        )

        if trophy_ids:
            celebrity.trophy.set(trophy_ids)

        return redirect("Celebrity")  
    
    elif request.method == "GET":
        form = CreateCelebrities()
    return render(request, "main/create.html", {"form":form})
  




        