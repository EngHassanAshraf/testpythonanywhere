from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.getRoutes),
    path('notes/', v.getNotes),
    path('notes/create/', v.createNote),
    path('notes/<str:pk>/', v.getNote),
    path('notes/<str:pk>/update/', v.updateNote),
    path('notes/<str:pk>/delete/', v.deleteNote),
    path('names/', v.getNames), 
]
