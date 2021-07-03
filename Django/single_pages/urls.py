from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]
