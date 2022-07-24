from rest_framework.views import Response
from rest_framework import viewsets
from rest_framework import generics

from ..models.component import Keyboard, Mouse, Display, Speaker, MotherBoard, Processor
from ..serializers.component import KeyboardSerializer, MouseSerializer, DisplaySerializer, SpeakerSerializer, MotherBoardSerializer, ProcessorSerializer 

# Create your views here.

class KeyboardViewSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer

class DisplayViewSet(viewsets.ModelViewSet):
    queryset = Display.objects.all()
    serializer_class = DisplaySerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class MotherBoardViewSet(viewsets.ModelViewSet):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherBoardSerializer

class ProcessorViewSet(viewsets.ModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer