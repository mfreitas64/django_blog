from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.views import generic
from datetime import datetime

from .models import Post 

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

#def calendario(request):
#    mycont = []
#    mycal = calendar.HTMLCalendar(firstweekday=0)
#    mycali = mycal.itermonthdays3(2022,11)
#    for c in mycali:
#        mycont.append(c)
#    context = {
#        'mycont': mycont
#    }
#    return render(request, 'blog/calendario.html', context)