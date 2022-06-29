from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


items = [
    {'id': 1, 'name': 'Chemistry 101'},
    {'id': 2, 'name': 'BIology 101'},
    {'id': 3, 'name': 'Literature 101'},
    {'id': 4, 'name': 'Mathematics 101'},
    {'id': 5, 'name': 'Physics 101'},
]
# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def room(request, pk):
    room = None
    for i in items:
        if i['id'] == int(pk):
            room = i
    context = {'rooms': items}
    return render(request, 'core/room.html', context)


def rooms(request):
    context = {'rooms': items}
    return render(request, 'core/rooms.html', context)