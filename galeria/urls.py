from django.urls import path
from galeria.views import index
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/', views.imagem, name='imagem'),
]