"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from basics.views import *
from basics import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("abc/",abc,name="abc"),
    path('led/',led,name="led"),
    path('counter/',counter,name="counter"),
    path('email/',email,name="email"),
    path('calci/',calci,name="calci"),
    path('Employee/',Employee,name="Employee"),
    path('Employee_View/',Employee_View,name="Employee_View"),
    path("Employee_update/<id>",Employee_update,name="Employee_update"),
    path("Employee_delete/<id>",Employee_delete,name="Employee_delete"),
    path("index/",index,name="index"),
    path("signup/",SignupPage,name="signup"),
    path("login/",LoginPage,name="login"),
    path("logout/",LogoutPage,name="logout"),
    path("predict/",predict,name="predict"),
    path('admin/', admin.site.urls),
    path('social/', social, name='social'),
    path('Classification/',Classification,name="Classification"),
    path('banana_leaf',banana_leaf,name="banana_leaf"),
    path('cinnamon',cinnamon,name="cinnamon"),
]


