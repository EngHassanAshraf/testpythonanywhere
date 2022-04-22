from rest_framework.serializers import ModelSerializer
from .models import Note, Name

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class NameSerializer(ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'