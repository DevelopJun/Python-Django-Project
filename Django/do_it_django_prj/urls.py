"""do_it_django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf import settings  # 이거를 하는 이유가, static 파일이랑 setting 파일을 사용해야하니까,
from django.conf.urls.static import static


urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    # 이게 첫 메인 화면인거지, path 가 공백이니까 8000포트 url 그대로
    path('', include('single_pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)  # 이미지 URL 등록한거임
