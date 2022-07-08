"""anime_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rest_framework.urlpatterns import format_suffix_patterns
from reviews_anime import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genre/', views.genre_list),
    path('genre/<int:pk>', views.genre_detail),
    path('anime/', views.anime_list.as_view()),
    path('anime/<int:pk>', views.anime_detail),
    path('reviews/', views.reviews_list.as_view()),
    path('reviews/<int:pk>', views.reviews_detail),
    path('star/', views.raitingStar_list.as_view()),
    path('star/<int:pk>', views.raitingStar_detail),
    path('raiting/', views.raiting_list.as_view()),
    path('raiting/<int:pk>', views.raiting_detail),
]
