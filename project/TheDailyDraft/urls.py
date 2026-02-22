from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MyHome, name='home'),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register')
]
