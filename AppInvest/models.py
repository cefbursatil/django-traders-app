from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import os

class Traders(models.Model):
    idTrader=models.IntegerField()
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"

class TradingStrategies(models.Model):
    nombre=models.CharField(max_length=40)
    activo = models.CharField(max_length=40) #En que activo se aplica la estrategia
    descripcion = models.CharField(max_length=140) #Descripción general de la estrategia
    trader=models.ForeignKey(User, on_delete=models.CASCADE)


class Trades(models.Model):
    #Choices type
    class TradeType(models.IntegerChoices):
        ENTRY = 0, 'Entry'
        EXIT = 1, 'Exit'
    
    class TradeDirection(models.IntegerChoices):
        BUY = 0, 'Buy'
        SELL = 1, 'Sell'
    strategy=models.ForeignKey(TradingStrategies, on_delete=models.CASCADE)
    activo=models.CharField(max_length=40)
    tradeDirection=models.IntegerField( choices=TradeDirection.choices)
    typeentry=models.IntegerField(default=TradeType.ENTRY, choices=TradeType.choices)
    precio = models.FloatField() #En que activo se aplica la estrategia
    descripcion = models.CharField(max_length=140) #Descripción general de la estrategia


class Avatar(models.Model):
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    
    avatar = models.ImageField(upload_to='avatar',null=True,blank=True)

    def __str__(self):
        return self.user.username
    
    def delete(self, using=None, keep_parents=False):
        self.avatar.storage.delete(self.avatar.name)
        super().delete()