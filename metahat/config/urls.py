"""
URL configuration for metahat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users.api.views import UserView

API_PREFIX = 'api/v1/'

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{API_PREFIX}", include("config.api_router"), name="api-root"),
    path(f"{API_PREFIX}users/", UserView.as_view(), name="user-create"),
    path(f"{API_PREFIX}transactions/", include("blockchain.api.urls")),
]
