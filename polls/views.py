# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.",content_type="text/plain")


from rest_framework import viewsets
from .models import Game
from .serializers import GameSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
