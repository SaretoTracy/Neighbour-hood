from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('profile-update',views.update_profile, name='update_profile'), 
    path('profile/<pk>',views.profile, name = 'profile'),
]
