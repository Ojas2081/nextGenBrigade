"""
URL configuration for nextGenBrigade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import *


urlpatterns = [
    path("", login_html, name="login_html"),
    path("signup/",register_html,name="register_html"),
    path("company/register/",CompanyRegisterAV.as_view(),name="register"),
    path("company/login/",CompanyLoginAV.as_view(),name="login"),
    path("nextGen-home/",home,name="home"),
]
