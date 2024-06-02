from django.urls import path
from .views import *

urlpatterns = [
    path('list-users', index, name='index'),
    # path('create-user', views.create, name='create'),
    # path('update-user', views.update, name='update'),
    # path('delete-user', views.delete, name='delete'),
    # path('detail-user', views.detail, name='detail'),
]
