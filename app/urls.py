from django.urls import path 
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.notes, name='notes'),
    path('new-note/', views.new_note, name='new-note'),
    path('note/<int:id>/', views.note, name='note'),
    path('note-update/<int:id>', views.note_update, name='note-update'),
    path('note-delete/<int:id>/', views.note_delete, name='note-delete'),
]
