from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer, NameSerializer
from .models import Note, Name


@api_view(['GET'])
def getRoutes(request):
    return Response([{1:"",2:""},
                         {1:"",2:""},
                         {1:"",2:""},
                         ],
                )
    
@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        id = data['id'],
        body = data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)
    

@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    
    serializer = NoteSerializer(note, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response(f"Note{pk} Deleted")

@api_view(['GET'])
def getNames(request):
    names = Name.objects.all()
    serializer = NameSerializer(names, many=True)
    return Response(serializer.data)