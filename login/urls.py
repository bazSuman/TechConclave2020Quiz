"""Quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from login import views
from .views import home, loginpage, register
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
    path('register/', views.register, name='register'),
    path('rougrnd1GA/', views.round1GA, name='round1GA'),
    path('rougrnd1GB/', views.round1GB, name='round1GB'),
    path('rougrnd1GC/', views.round1GC, name='round1GC'),
    path('rougrnd1GD/', views.round1GD, name='round1GD'),
    path('rougrnd1GE/', views.round1GE, name='round1GE'),
    path('cfcquizfinale/', views.grandfinale, name='grandfinale'),
    path('finalegr/', views.finalegr, name='finalegr'),
    path('finalebr/', views.finalebr, name='finalebr'),
    path('finalerr/', views.finalerr, name='finalerr'),
    # path('rougrnd1GF/', views.round1GF, name='round1GF'),
    # path('rougrnd1GG/', views.round1GG, name='round1GG'),
    # path('rougrnd1GH/', views.round1GH, name='round1GH'),
    # path('rougrnd1GI/', views.round1GI, name='round1GI'),
    # path('rougrnd1GJ/', views.round1GJ, name='round1GJ'),
]
