"""gurushishya URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from website import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base,),
    path('home/', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('enterotp/', views.enterotp, name = 'enterotp'),
    path('profile/', views.profile, name = 'profile'),
    path('modal/', views.modal, name = 'modal'),
    path('password_reset/', views.password_reset, name = 'password_reset'),
    path('password_reset_done/', views.password_reset_done, name = 'password_reset_done'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
