"""Investar URL Configuration

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
from hello import views # hello 앱의 views를 임포트 한 뒤
from django.urls import path, re_path # django.urls로 부터 re_path() 함수를 추가적으로 임포트 한다.

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<name>[A-Z][a-z]*)$', views.sayHello), # urlpatterns 리스트의 마지막에 hello 앱의 URL에 대한 뷰 처리를 추가한다. 
]
