from django.conf.urls import include, url
from rest_framework import routers
from . import views

todo_router = routers.DefaultRouter()
todo_router.register(r'todos', views.TodoViewSet, base_name='todos')
todo_router.register(r'out_source_task',
                     views.OutSourceTaskViewSet, base_name='out_source_task')
todo_router.register(r'carouse',
                     views.CarouselViewSet, base_name='carouse')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('^api/', include(todo_router.urls)),
]
