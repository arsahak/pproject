from django.urls import path
from django.conf.urls import url
from my_app import views

urlpatterns = [
    path('/', views.index, name = 'index'),

]
