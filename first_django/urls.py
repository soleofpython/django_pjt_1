"""first_django URL Configuration

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
from django.conf.urls.static import static

from creative.views import write, articleList
from . import views
from .views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    # path('', include('single_page.urls')),
    # path('creative/', include('creative.urls')),
    path('dashboard/', include('dashboard.urls')),
    # path('', include('single_pages.urls')),

    path('write/', write, name='write'),
    path('', views.index, name='index'),
    path('list/', articleList, name="list"),
    # django.contrib.auth.urls 장고 내장 인증 urls 활용
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    # 가입처리
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    # 계정생성이 완료됐다는 메시지를 보여줌
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)