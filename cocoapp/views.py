from django.shortcuts import render
from . import dao

from cocoapp.models import User, Saving
from rest_framework import viewsets
from coco.serializers import UserSerializer, SavingSerializer

def index(request):
    posts = dao.selectTest()
    return render(request, 'cocoapp/index.html', {'posts' : posts})


# user table api
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# saving table api
class SavingViewSet(viewsets.ModelViewSet):
    queryset = Saving.objects.all()
    serializer_class = SavingSerializer