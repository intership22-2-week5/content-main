from rest_framework import serializers
from ..models.computer import Computer
from ..models.component import Display, MotherBoard, Processor, Keyboard, Mouse, Speaker


class ComputerSerializer(serializers.ModelSerializer):
    display = serializers.PrimaryKeyRelatedField(many=False, queryset=Display.objects.all())
    speaker = serializers.PrimaryKeyRelatedField(many=False, queryset=Speaker.objects.all())
    mouse = serializers.PrimaryKeyRelatedField(many=False, queryset=Mouse.objects.all())
    keyboard = serializers.PrimaryKeyRelatedField(many=False, queryset=Keyboard.objects.all())
    motherboard = serializers.PrimaryKeyRelatedField(many=False, queryset=MotherBoard.objects.all())
    processor = serializers.PrimaryKeyRelatedField(many=False, queryset=Processor.objects.all())
    class Meta:
        model = Computer
        fields = '__all__'
        depth = 1
        read_only_fields = ('create_at', 'update_at')
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'total_cost': instance.total_cost,
            'cantidad': instance.quantity,
            'components': {
                'display': {
                    'id': instance.display.id,
                    'mark': instance.display.mark,
                    'description': instance.display.description,
                    'cost': instance.display.cost,
                },
                'speaker': {
                    'id': instance.speaker.id,
                    'mark': instance.speaker.mark,
                    'description': instance.speaker.description,
                    'cost': instance.speaker.cost,
                },
                'mouse': {
                    'id': instance.mouse.id,
                    'mark': instance.mouse.mark,
                    'description': instance.mouse.description,
                    'cost': instance.mouse.cost,
                },
                'keyboard': {
                    'id': instance.keyboard.id,
                    'mark': instance.keyboard.mark,
                    'description': instance.keyboard.description,
                    'cost': instance.keyboard.cost,
                },
                'motherboard': {
                    'id': instance.motherboard.id,
                    'mark': instance.motherboard.mark,
                    'description': instance.motherboard.description,
                    'cost': instance.motherboard.cost,
                },
                'processor': {
                    'id': instance.processor.id,
                    'mark': instance.processor.mark,
                    'description': instance.processor.description,
                    'cost': instance.processor.cost,
                }
            },
            'create_at': instance.create_at
        }

