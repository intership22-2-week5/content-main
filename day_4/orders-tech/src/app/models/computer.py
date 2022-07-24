from django.db import models

from .component import Display, Keyboard, Mouse, Speaker, MotherBoard, Processor

class Computer(models.Model):
    name = models.CharField(max_length=50)
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(MotherBoard, on_delete=models.CASCADE)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_cost = models.FloatField(null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

  
    def save(self, *args, **kwargs):
        result_decrement = self.decrement_quantity()
        if type(result_decrement) == int or type(result_decrement) == float:
            self.total_cost = result_decrement
            super(Computer, self).save(*args, **kwargs)
            return True
        else:
            raise Exception(result_decrement)

    def decrement_quantity(self):
        cost = 0
        keyboard = Keyboard.objects.get(id=self.keyboard.id)
        mouse = Mouse.objects.get(id=self.mouse.id)
        display = Display.objects.get(id=self.display.id)
        speaker = Speaker.objects.get(id=self.speaker.id)
        motherBoard = MotherBoard.objects.get(id=self.motherboard.id)
        processor = Processor.objects.get(id=self.processor.id)
        #targeta = TargetaderReda.objects.get(id=self.targetader_reda.id)
        
        components = [keyboard, mouse, display, speaker, motherBoard, processor]
        
        quantity_less = [component for component in components if component.quantity < self.quantity]
        if len(quantity_less) > 0:
            component_less = {}
            for component in quantity_less:
                component_less[component.type_component] = component.quantity
            return component_less
        else:
            for component in components:
                cost += component.cost
                component.quantity -= self.quantity
                component.save()
            return cost

    def update_quantity(self, quantity):
        self.quantity = quantity
        super(Computer, self).save()