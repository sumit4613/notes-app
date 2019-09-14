from rest_framework import generics

from .models import Note
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    """
    Creates ListAPI which list all objects of the model Note
    """
    queryset = Note.objects.all().order_by('-created', '-updated')
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Created DetailAPI which gives the details 
    of the objects of Note Model
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
