from django.urls import path
from . import views

urlpatterns = [
    path('notes/all', views.all_notes_list.as_view()),
    path('notes/create', views.create_notes_list.as_view()),
    path('track/all', views.all_chart_list.as_view()),
    path('track/create', views.create_chart_list.as_view()),
    path('link/all', views.all_link_list.as_view()),
    path('link/create', views.create_link_list.as_view()),

    # Auth
    path('createUser', views.register),
    path('loginUser', views.loginUser)

]