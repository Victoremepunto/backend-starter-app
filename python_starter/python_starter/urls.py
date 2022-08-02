"""python_starter URL Configuration

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
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('healthz', views.health),
    path('livez', views.liveness),
    path('readyz', views.readiness),
    path('kafka', views.handle_kafka),
    path('minio', views.handle_minio),
    path('redis', views.handle_redis),
    path('postgres', views.handle_postgres),
    path('postgres_init', views.postgres_init_get),
    path('featureflag', views.feature_flag_get),
]
views.start_app()
