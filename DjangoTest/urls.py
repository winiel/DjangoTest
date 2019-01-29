"""DjangoTest URL Configuration

The `urlpatterns` list routes URLs to dt_view. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function dt_view
    1. Add an import:  from my_app import dt_view
    2. Add a URL to urlpatterns:  path('', dt_view.home, name='home')
Class-based dt_view
    1. Add an import:  from other_app.dt_view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestViews import views


urlpatterns = [
    path('', views.index),
    # path('admin/', admin.site.urls),
]
