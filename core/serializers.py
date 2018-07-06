from core.models import Carousel
from rest_framework import serializers


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
