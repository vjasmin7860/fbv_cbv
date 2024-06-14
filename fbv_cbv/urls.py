"""
URL configuration for fbv_cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('string_by_fbv/',string_by_fbv,name='string_by_fbv'),
    path('StringByCbv/',StringByCbv.as_view(),name='StringByCbv'),



    path('html_by_fbv/',html_by_fbv,name='html_by_fbv'),
    path('HtmlByCbv/',HtmlByCbv.as_view(),name='HtmlByCbv'),




    path('insert_by_fbv/',insert_by_fbv,name='insert_by_fbv'),
    path('Insert_By_Cbv/',Insert_By_Cbv.as_view(),name='Insert_By_Cbv'),



    path('Html_By_Tv/',Html_By_Tv.as_view(),name='Html_By_Tv'),
    
]
