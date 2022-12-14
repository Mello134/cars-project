"""cars URL Configuration

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
from django.urls import path, include
from django.conf import settings
#импортировали сеттингс для того чтобы было видн media url and root
from django.conf.urls.static import static
#тоже добавили
#Эти строчки кода используются для управления любыми медиафайлами включая видео
import home.views


urlpatterns = [
    path('admin/', admin.site.urls),     
    path('', home.views.home, name='home'),#в home/views.py - функция home, применили имя home
    path('posts/', include('blog.urls')),#ссылка на urls.py в приложении блога

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
