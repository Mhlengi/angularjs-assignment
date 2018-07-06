from django.shortcuts import render
from rest_framework import viewsets
import json

import logging

from jsframework.models import (
    Carousel,
    OutSourceTask,
    Todo
)
from jsframework.serializers import (
    CarouselSerializer,
    OutSourceTaskSerializer,
    TodoSerializer
)


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class OutSourceTaskViewSet(viewsets.ModelViewSet):
    queryset = OutSourceTask.objects.all()
    serializer_class = OutSourceTaskSerializer


class CarouselViewSet(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = CarouselSerializer


def index(request):
    update_json(request)
    return render(request, 'jsframework/base.html')


def update_json(request):
    with open('jsframework/static/json/data.json') as data_file:
        data = json.load(data_file)
        try:
            OutSourceTask.objects.get_or_create(description=data)
        except Exception as e:
            logging.error(e)
