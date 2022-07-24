from django.db import models

# Create your models here.

class Component(models.Model):
    component =(
      ('keyboard','teclado'),
      ('mouse','raton'),
      ('display', 'monitor'),
      ('speaker', 'altavoz'),
      ('motherboard', 'placa'),
      ('processor', 'procesador')
    )
    type_component = models.CharField(max_length=20, choices=component)

    def __str__(self):
        return self.type_component

class InputDevice(Component):
    mark = models.CharField(max_length=50)
    def __str__(self):
        return self.mark

class Keyboard(InputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.mark

class Mouse(InputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.mark

class OutputDevice(Component):
    mark = models.CharField(max_length=50)
    def __str__(self):
        return self.mark

class Display(OutputDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.mark

class Speaker(OutputDevice):
    quantity = models.IntegerField()
    cost = models.IntegerField()
    description = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.mark

class InternalDevice(Component):
    mark = models.CharField(max_length=50)
    def __str__(self):
        return self.mark


class MotherBoard(InternalDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.mark

class Processor(InternalDevice):
    quantity = models.IntegerField()
    cost = models.FloatField()
    description = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.mark