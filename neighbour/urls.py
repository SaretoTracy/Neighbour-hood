"""neighbour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views 
from django.urls import path
from hood import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome, name='welcome'),
    path('index',views.index, name='index'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile-update',views.update_profile, name='update_profile'),
    path('profile/<pk>',views.profile, name = 'profile'),
    path('create-hood',views.createhood, name='createhood'), 
    path('hood/<id>',views.neighbourhood, name = 'neighbourhood'),
    path('join_neighbourhood/<id>', views.join_neighbourhood, name='join-neighbourhood'),
    path('business/<id>',views.createbusiness, name = 'create-business'),
    path('post/<hood_id>',views.post, name = 'post'),
    path('change_neighbourhood/<id>', views.change_neighbourhood, name='change-neighbourhood'),
    path('search/',views.search_results, name='search_results'),
    path('logout/', views.logout_user, name='logout'),


]
