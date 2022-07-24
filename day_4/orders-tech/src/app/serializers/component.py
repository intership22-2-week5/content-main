from rest_framework import serializers

#
from ..models.component import Component, InputDevice, OutputDevice, InternalDevice ,Keyboard, Mouse, Display, Speaker, MotherBoard, Processor


class InputDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputDevice
        fields = '__all__'

class OutputDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutputDevice
        fields = '__all__'

class InternalDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalDevice
        fields = '__all__'


class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'

class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = '__all__'

class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Display
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'


class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = '__all__'

class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        exclude = ('type_component',)
