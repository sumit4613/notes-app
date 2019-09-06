from rest_framework import serializers

from . models import Note


class NoteSerializer(serializers.ModelSerializer):
    """[summary]
    This converts all the data into JSON object
    """
    class Meta:
        model = Note
        fields = '__all__'
