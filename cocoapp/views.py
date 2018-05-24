from django.shortcuts import render
from . import dao

def index(request):
    posts = dao.selectTest()
    return render(request, 'cocoapp/index.html', {'posts' : posts})
