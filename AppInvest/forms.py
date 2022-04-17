from django import forms
from .models import Avatar

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
        
    def clean_email(self):
      email = self.cleaned_data.get('email')
      if User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'El email ya está registrado,prueba con otro.')
      return email

#para editar solamente los datos del usuario
class UserEditForm(forms.ModelForm):
    # Obligatorio
    email = forms.EmailField()
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

#para editar solamente la contraseña
class UserEditPass(UserCreationForm):
    # # Obligatorio
    # email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email','password1', 'password2']

#para editar avatar
class UploadImageForm(forms.ModelForm):
    avatar = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ['avatar']
    
    # def clean_avatar(self):
    #     avatar = self.cleaned_data['avatar']
    #     return avatar