"""myproject URL Configuration

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
from django.urls import path,include
from memo.views import index,second
from django.conf import settings #settings에 접근하기 위해 불러옴
from django.conf.urls.static import static #static한 url을 만들어주기위해서 가져옴
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('memo/',include('memo.urls')),  #memo앱과 관련된 url은 memo 앱 밑에 있는 urls.py에서 관리해줍시다.
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
# 쉽게 이해를 해보자면 기존에 있는 url규칙들에 새로운 규칙을 추가해주는건데
# MEDIA_URL로 사용자가 요청하면 MEDIA_ROOT에 있는 document들을 제공해주자 라는 의미정도로 해석합시다.

