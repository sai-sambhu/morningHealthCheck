"""basicform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from basicfromapp import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^updateTime/',views.indexChange,name='indexChange'),
    
    url(r'^hello/',views.form_name_view,name='form'),
    url(r'^get_todo/',views.get_todo,name='get_todo'),
    url(r'^add_todo/',views.add_todo,name='add_todo'),
    url(r'^update/',views.update,name='update'),
   url(r'^updatepage/',views.updatepage,name='updatepage'),
   url(r'^ForLoopTest/',views.ForLoopTest,name='ForLoopTest'),
   url(r'^ForLoopTestPage/',views.ForLoopTestPage,name='ForLoopTestPage'),
   
    
    url('admin/', admin.site.urls),
]
