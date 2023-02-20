from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from .models import ToDoList, Items
from. forms import CreateNewList

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls":ls})

#def index(response, id):
 #   return HttpResponse("<h1>%s</h1>"% id)   #its a first way of a dynamic pages in terms of linking

  
def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            v = ToDoList(name=n)
            v.save()
        return HttpResponseRedirect("/%i" %v.id)

    else:
        form = CreateNewList()

    return render(response,"main/create.html", {"form":form} )

