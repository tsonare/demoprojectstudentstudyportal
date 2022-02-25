from django.urls import path
from .import views

urlpatterns = [
    path('home_authenticated', views.home_authenticated, name = "home_authenticated"),   
    path('', views.home_not_authenticated, name = "home_not_authenticated"),   
    path('notes', views.notes, name = "notes"),    
    path('delete_note/<int:pk>', views.delete_note, name = "delete_note"),    
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view(), name = "notes_detail"),
    path('edit_note/<int:pk>', views.edit_note, name = "edit_note"),
]
