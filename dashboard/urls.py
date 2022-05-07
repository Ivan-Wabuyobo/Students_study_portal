import imp
from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="home"),
    path('notes/', views.notes, name="notes"),
    path('notes/notes_detail/<int:pk>', views.notes_detail, name='notes-detail'), 
    path('delete_notes/<int:pk>', views.delete_notes, name="delete-notes"),
    path('homework', views.homework, name="home-work"),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete-homework'),
    path('youtube/', views.youtube, name="youtube"),
    path('dictionary/', views.dictionary, name='dictionary')
    
]