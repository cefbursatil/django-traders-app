from django import forms

class TradeForm(forms.Form):

    idTrade=forms.IntegerField()
    activo=forms.CharField(max_length=40)
    tradeDirection=forms.IntegerField()
    typeentry=forms.IntegerField()
    precio = forms.FloatField() #En que activo se aplica la estrategia
    descripcion = forms.CharField(max_length=140) #Descripción general de la estrategia

class TradingStrategyForm(forms.Form):
    idStrategy=forms.IntegerField()
    nombre=forms.CharField(max_length=40)
    activo = forms.CharField(max_length=40) #En que activo se aplica la estrategia
    descripcion = forms.CharField(max_length=140) #Descripción general de la estrategia


class TradersForm(forms.Form):
    idTrader=forms.IntegerField()
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
