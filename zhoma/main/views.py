from django.shortcuts import render , redirect
from .models import Celebrities , Trophy, Club
from .form import CreateCelebrities
# Create your views here.

def celebrity_list(request):
    if request.method == "GET":
        celebrities = Celebrities.objects.all()
        return render(request , 'main/index.html',{'celebrities' : celebrities })


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
        form = CreateCelebrities
        return render(request, "main/create.html", {"form":form})


    clubs = Club.objects.all()
    trophies = Trophy.objects.all()
    return render(request, "main/create.html", {
        "clubs": clubs,
        "trophies": trophies
    })
  




        