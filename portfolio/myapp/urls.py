from django.urls import path
from . import views
from .views import create_contact

urlpatterns = [
    path('', views.index, name='index'),
    path('api/contact' , create_contact , name='create_contact')
]



