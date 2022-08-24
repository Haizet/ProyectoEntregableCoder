"""AppCoderEntregable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from AppCoderMarianoVanetta.views import crear_familia, ver_familia,crear_familia_parm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_familia/', crear_familia),
    path('ver_familia/', ver_familia),
    path('crear_familia_parm/<nombre>/<apellido>/<edad>/<padre>', crear_familia_parm)
]
