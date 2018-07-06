from django.conf.urls import include, url
from rest_framework import routers
from . import views

carousel_router = routers.DefaultRouter()
carousel_router.register(
    r'carousels',
    views.CarouselViewSet,
    base_name='carousels'
)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^api/', include(carousel_router.urls)),
]
