from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.NoteList.as_view()),  # api/v1/notes
    path('<int:pk>/', views.NoteDetail.as_view()),  # api/v1/notes/1
]
