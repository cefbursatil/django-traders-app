from django import forms

class TradeForm(forms.Form):

    idTrade=forms.IntegerField()
    activo=forms.CharField(max_length=40)
    tradeDirection=forms.IntegerField()
    typeentry=forms.IntegerField()
    precio = forms.FloatField() #En que activo se aplica la estrategia
    descripcion = forms.CharField(max_length=140) #Descripción general de la estrategia

class TradingStrategyForm(forms.Form):
    nombre=forms.CharField(max_length=40)
    activo = forms.CharField(max_length=40) #En que activo se aplica la estrategia
    descripcion = forms.CharField(max_length=140) #Descripción general de la estrategia


class TradersForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()


#USUARIOs LOGIN
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    # Obligatorio
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']

