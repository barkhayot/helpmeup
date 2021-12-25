from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.allNotes, name='allNotes'),
    path('createNote/', views.createNote, name='createNote'),
    path('noteDetail/<int:pk>', views.noteDetail, name='noteDetail'),
    path('noteDelete/<int:pk>', views.noteDelete, name='noteDelete')
    
]