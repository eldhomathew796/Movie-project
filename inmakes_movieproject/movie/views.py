from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import Movie
from .forms import *
# Create your views here.


def index(request):

    obj = Movie.objects.all()
    context = {
        'i_obj': obj
    }
    return render(request, 'index.html', context)


def detailview(request, id):
    print(id)
    obj = Movie.objects.get(id=id)
    context = {
        'obj': obj
    }
    return render(request, 'details.html', context)


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']

        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
        

    return render(request, 'add_movie.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    movie=Movie.objects.get(id=id)
    movie.delete()
    return redirect('index')

    
