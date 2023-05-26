"""
URL configuration for backend project.

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

from backend.views import get_user
from backend.views import get_plane
from backend.views import login_view
from backend.views import register_view
from backend.views import get_planes
from backend.views import add_planes
urlpatterns = [
    path("admin/", admin.site.urls),
    path('users/<int:user_id>/', get_user, name='get_user'),
    path('planes/<int:plane_id>/', get_plane, name='get_plane'),
    path('planes/', get_planes, name='get_planes'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register'),
    path('addplanes/', add_planes, name='add_planes'),


]
