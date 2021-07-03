from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index),  # 함수명 꼭 index가 아니어도 상관없습니다. 함수명을 소문자로 만드는 습관은 있다.
]
