from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    #On affiche toutes les publications sans entrer dans les details
    pubs = Publication.objects.all()
    
    context = {
        "pubs" : pubs,
    }

    return render(request, "Forum/index.html", context)

def create(request):
    if request.method == 'POST':
        pub = Publication(
            Title = request.POST['Title'],
            Content = request.POST['Content'],
            Pub_User = request.user,
            Theme = request.POST['Theme']
        )
        pub.save()
        return HttpResponse("Publication crée")

    return render(request, "Forum/form.html")

    
def read(request, id):
    pub = get_object_or_404(Publication, id=id)
    comments = Comment.objects.filter(Subject_Id = pub.id)
    try:
        progress = (pub.Likes/(pub.Dislikes + pub.Likes))*100
    except:
        progress = 0
    
    context = {
        "pub" : pub,
        "progress" : progress,
        "comments" : comments,
    }

    return render(request, "Forum/read.html", context)


def modify(request, id):
    pub = get_object_or_404(Publication, id=id)
    if request.method == 'POST':
        pub.Title = request.POST['Title'],
        pub.Content = request.POST['Content'],
        Theme = request.POST['Theme']
        
        pub.save()
        return redirect("readMore", id)

    context = {
        "pub" : pub,
        "modifying" : True,
    }
    return render(request, "Forum/form.html", context)


def delete(request, id):
    pub = get_object_or_404(Publications, id=id)
    pub.delete()

    redirect("home")