from django.urls import path
from . import views

app_name = 'ProfileView'
urlpatterns = [
    path('', views.index, name='index'),
]