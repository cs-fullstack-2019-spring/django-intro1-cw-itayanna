


# importhing path function

from django.urls import path

# importing the views file that has all the responses

from . import views

# all the paths you can take within the server

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music, name='Music'),
    path('chronixx/', views.chronixx, name='Chronixx'),
    path('laurynhill/', views.laurynHill, name='Lauryn Hill'),
    path('jojo/',views.jojo, name='JoJo')

]