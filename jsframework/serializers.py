from rest_framework import serializers
from jsframework.models import Carousel, OutSourceTask, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo


class OutSourceTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutSourceTask


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
