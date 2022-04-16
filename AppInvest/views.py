from django.conf import settings
import email
from django.shortcuts import render, HttpResponse,HttpResponseRedirect,redirect

from django.http import HttpResponse
from AppInvest.models import Trades, TradingStrategies, Traders
from AppInvest.forms import TradeForm, TradingStrategyForm, TradersForm
# Para el login
from AppInvest.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



#@login_required
def inicio(request):

    return render(request, "AppInvest/inicio.html")


# TRADERS
@login_required
def traders(request):

    traders = Traders.objects.all()
    # trae todos los profesores
    if request.method == 'POST':
        miFormulario = TradersForm(request.POST)
        # aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:
            # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            trader = Traders(idTrader=informacion['idTrader'], nombre=informacion['nombre'],
                             apellido=informacion['apellido'], email=informacion['email'])
            trader.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppInvest/inicio.html")
    else:
        miFormulario = TradersForm()  # Formulario vacio para construir el html
    contexto = {"traders": traders, "miFormulario": miFormulario}
    return render(request, "AppInvest/traders.html", contexto)

# Muestra los Traders Registrados

@login_required
def listTraders(request):
    traders = Traders.objects.all()
    contexto = {"traders": traders}
    return render(request, "AppInvest/list_traders.html", contexto)

@login_required
def eliminarTrader(request, trader_id):
    #trader = Traders.objects.get(idTrader=trader_id)
    trader = Traders.objects.get(id=trader_id)
    trader.delete()
    # vuelvo al menú
    traders = Traders.objects.all()  # trae todos los profesores
    contexto = {"traders": traders}
    return render(request, "AppInvest/list_traders.html", contexto)

@login_required
def editarTrader(request, trader_id):
    # Recibe el nombre del profesor que vamos a modificar
    #trader = Traders.objects.get(idTrader=trader_id)
    trader = Traders.objects.get(id=trader_id)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = TradersForm(request.POST)

        # print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            print(miFormulario)
            informacion = miFormulario.cleaned_data
            trader.nombre = informacion['nombre']
            trader.apellido = informacion['apellido']
            trader.email = informacion['email']
            trader.save()
            # Vuelvo al inicio o a donde quieran
            traders = Traders.objects.all()
            contexto = {"traders": traders}
            return render(request, "AppInvest/list_traders.html", contexto)
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        # miFormulario = TradersForm(initial={'idTrader': trader.idTrader,'nombre': trader.nombre, 'apellido': trader.apellido,
        #                      'email': trader.email})
        miFormulario = {'idTrader': trader.idTrader, 'nombre': trader.nombre, 'apellido': trader.apellido,
                        'email': trader.email}
    # Voy al html que me permite editar
    return render(request, "AppInvest/editartrader.html", {"miFormulario": miFormulario, "id": trader_id})

#################################################

@login_required
def listTrades(request, tradingstrat_id):
    traders = Trades.objects.filter(strategy=tradingstrat_id)
    contexto = {"trades": trades}
    return render(request, "AppInvest/list_trades.html", contexto)

@login_required
def trades(request):

    if request.method == 'POST':
        miFormulario = TradeForm(request.POST)
        # aquí mellega toda la información del html
        print(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            # Falta Traer el foreign key
            trade = Trades(idTrade=informacion['idTrade'], activo=informacion['activo'], tradeDirection=informacion['tradeDirection'],
                           typeentry=informacion['typeentry'], precio=informacion['precio'], descripcion=informacion['descripcion'])
            trade.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppInvest/inicio.html")
    else:
        miFormulario = TradeForm()  # Formulario vacio para construir el html
    return render(request, "AppInvest/trades.html", {"miFormulario": miFormulario})


# TRADING STRATEGIES

@login_required
def listTradingStrategies(request):
    tradingstrat = TradingStrategies.objects.filter(trader=request.user.id)
    contexto = {"tradingstrat": tradingstrat}
    return render(request, "AppInvest/list_trading_strat.html", contexto)

@login_required
def eliminarTradingStrat(request, tradingstrat_id):
    #trader = Traders.objects.get(idTrader=trader_id)
    tradingstrat = TradingStrategies.objects.get(id=tradingstrat_id)
    tradingstrat.delete()
    # vuelvo al menú
    tradingstrat = TradingStrategies.objects.filter(trader=request.user.id)
    contexto = {"tradingstrat": tradingstrat}
    return render(request, "AppInvest/list_trading_strat.html", contexto)

@login_required
def editarTradingStrat(request, tradingstrat_id):
    # Recibe el nombre del profesor que vamos a modificar
    #trader = Traders.objects.get(idTrader=trader_id)
    tradingstrat = TradingStrategies.objects.get(id=tradingstrat_id)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = TradingStrategyForm(request.POST)

        # print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            print(miFormulario)
            informacion = miFormulario.cleaned_data
            tradingstrat.nombre = informacion['nombre']
            tradingstrat.apellido = informacion['activo']
            tradingstrat.descripcion = informacion['descripcion']
            tradingstrat.trader = request.user
            tradingstrat.save()
            # Vuelvo al inicio o a donde quieran
            tradingstrats = TradingStrategies.objects.filter(
                trader=request.user.id)
            contexto = {"tratradingstratdtradingstraters": tradingstrats}
            return render(request, "AppInvest/list_trading_strat.html", contexto)
        # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        # miFormulario = TradersForm(initial={'idTrader': trader.idTrader,'nombre': trader.nombre, 'apellido': trader.apellido,
        #                      'email': trader.email})
        miFormulario = {'nombre': tradingstrat.nombre, 'activo': tradingstrat.activo, 'descripcion': tradingstrat.descripcion,
                        'trader': request.user}
    # Voy al html que me permite editar
    return render(request, "AppInvest/editartradingstrat.html", {"miFormulario": miFormulario, "id": tradingstrat_id})

@login_required
def tradingstrategies(request):
    if request.method == 'POST':
        miFormulario = TradingStrategyForm(request.POST)
        # aquí mellega toda la información del html
        print(miFormulario)
        if miFormulario.is_valid:
            # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            # Falta Traer el foreign key
            tradingstrat = TradingStrategies(
                nombre=informacion['nombre'], activo=informacion['activo'], descripcion=informacion['descripcion'], trader=request.user)
            tradingstrat.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppInvest/list_trading_strat.html")
    else:
        miFormulario = TradingStrategyForm()  # Formulario vacio para construir el html
    return render(request, "AppInvest/tradingstrategies.html", {"miFormulario": miFormulario})

# LOGIN y REGISTRO

# Vista de login

def login_request(request):

    redirect_to = request.GET.get('next', '')
    if request.user.is_authenticated:
        return HttpResponseRedirect("/",locals())

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if redirect_to:
                        return HttpResponseRedirect(redirect_to,{"mensaje": f"Bienvenido {usuario}"})
                    else:
                        return HttpResponseRedirect("/",locals(),{"mensaje": f"Bienvenido {usuario}"})
                    #return HttpResponseRedirect("/",locals())
                    #return render(request, "AppInvest/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
        else:
            # form.add_error(None, 'Usuario y/o Contraseña incorrecta')#agrega mensaje
            pass
    else:
        form = AuthenticationForm()

    return render(request, "AppInvest/login.html", {"form": form})

def logout_request(request):
    logout(request)
    return HttpResponseRedirect("/",locals())

def register(request):

    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponseRedirect("login",locals())

    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, "AppInvest/registro.html",  {"form": form})


# Vista de editar el perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            return render(request, "AppInvest/inicio.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AppInvest/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
