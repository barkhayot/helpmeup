from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allURL, name='allURL'),
    path('createURL/', views.createURL, name='createURL'),
    path('URLDetail/<int:pk>', views.URLDetail, name='URLDetail'),
    path('URLDelete/<int:pk>', views.URLDelete, name='URLDelete'),
]