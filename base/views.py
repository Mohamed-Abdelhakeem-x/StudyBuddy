from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, 'name':'lets learn Python!'},
    {'id':2, 'name':'lets learn C++!'},
    {'id':3, 'name':'lets learn Go!'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')