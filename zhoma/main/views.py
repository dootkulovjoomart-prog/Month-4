from django.shortcuts import render , redirect
from .models import Celebrities , Trophy, Wife, Club

# Create your views here.

def celebrity_list(request):
    celebrities = Celebrities.objects.all()
    return render(request , 'main/index.html',{'celebrities' : celebrities })


def look_detail(request , id ):
    detail = Celebrities.objects.get(id=id)
    return render(request , 'main/detail_look.html' ,  {'celebrities' : detail })   

def nav_bar(request):
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
        wife_id = request.POST.get("wife")
        trophy_ids = request.POST.getlist("trophy")  # получаем список выбранных трофеев

        club = Club.objects.get(id=club_id) if club_id else None
        wife = Wife.objects.get(id=wife_id) if wife_id else None

        celebrity = Celebrities.objects.create(
            name=name,
            image=image,
            profession=profession,
            discription=discription,
            content=content,
            date=date,
            club=club,
            wife=wife
        )

        if trophy_ids:
            celebrity.trophy.set(trophy_ids)

        return redirect("celebrities_list")  


    clubs = Club.objects.all()
    wives = Wife.objects.all()
    trophies = Trophy.objects.all()
    return render(request, "main/create.html", {
        "clubs": clubs,
        "wives": wives,
        "trophies": trophies
    })

        