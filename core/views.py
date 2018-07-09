import json
import logging

from core.models import (
    OutSourceTask,
    Carousel
)
from core.serializers import CarouselSerializer
from django.contrib.auth import logout
from django.shortcuts import render
from rest_framework import viewsets


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer


def index(request):
    if request.user.is_authenticated():
        logout(request.user)
    update_json(request)
    return render(request, 'core/index.html')


def update_json(request):
    with open('core/static/json/data.json') as data_file:
        data = json.load(data_file)
        try:
            OutSourceTask.objects.get_or_create(description=data)
        except Exception as e:
            logging.error(e)
