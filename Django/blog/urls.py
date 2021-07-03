from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),

    # 만약에 지금 이게 붙어 있으면, pk라는 변수에 담아서 single_post_page() 함수로 넘기겠다는 말임.
    # path('<int:pk>/', views.single_post_page),
    # 함수명 꼭 index가 아니어도 상관없습니다. 함수명을 소문자로 만드는 습관은 있다. # 여기서는 지금 /blog/ 뒤에 아무것도 없으면
    # path('', views.index),
    # view에 index 함수 불러 오겠다는 말이고,
]
