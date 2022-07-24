from rest_framework import viewsets
from rest_framework.views import Response

from ..models.component import Keyboard, Mouse, Display, Speaker, MotherBoard, Processor
from ..models.computer import Computer
from ..models.component import Component, InputDevice, OutputDevice, InternalDevice
from ..serializers.component import KeyboardSerializer, MouseSerializer, DisplaySerializer, SpeakerSerializer, MotherBoardSerializer, ProcessorSerializer
from ..serializers.computer import ComputerSerializer
from ..serializers.component import ComponentSerializer, InputDeviceSerializer, OutputDeviceSerializer, InternalDeviceSerializer

class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return Response({'status': True, 'message': 'Computer created successfully'})
        except Exception as e:
            return Response({'status': False, 'message': str(e)})

    







class ComponentsViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

    def list(self, request, *args, **kwargs):
        try:
            search_component = request.data.get('search_component')
            if search_component == 'keyboard':
               return self.search_components(Keyboard, KeyboardSerializer,search_component)
            elif search_component == 'mouse':
                return self.search_components(Mouse, MouseSerializer, search_component)
            elif search_component == 'display':
                return self.search_components(Display, DisplaySerializer, search_component)
            elif search_component == 'speaker':
                return self.search_components(Speaker, SpeakerSerializer, search_component)
            elif search_component == 'motherboard':
                return self.search_components(MotherBoard, MotherBoardSerializer, search_component)
            elif search_component == 'processor':
                return self.search_components(Processor, ProcessorSerializer, search_component)
            elif search_component == 'outputdevice':
                return self.search_components(OutputDevice, OutputDeviceSerializer, None)
            elif search_component == 'inputdevice':
                return self.search_components(InputDevice, InputDeviceSerializer, None)
            else:
                return Response({'status': False, 'message': 'Component not found'})
        except Exception as e:
            return Response({'status': False, 'message': str(e)})

    def search_components(self, instance_model,serializar_search, search):
        try:
            components = None
            if search:
                components = instance_model.objects.filter(type_component=search)
            else:
                components = instance_model.objects.all()
            serializer = serializar_search(components, many=True)
            return Response({'status': True, 'message': 'Components found', 'data': serializer.data})
        except Exception as e:
            return Response({'status': False, 'message': str(e)})