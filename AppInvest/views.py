from xml.parsers.expat import model
from django.conf import settings
import email
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect

from django.http import HttpResponse
from AppInvest.models import Avatar, Trades, TradingStrategies, Traders,User
from AppInvest.forms import TradeForm, TradingStrategyForm, TradersForm, UserEditPass,UploadImageForm
# Para el login
from AppInvest.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash

from django.contrib import messages
import io,csv

# @login_required
def inicio(request):

    return render(request, "AppInvest/inicio.html")

# @login_required
def about(request):

    return render(request, "AppInvest/about.html")

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

##trades

@login_required
def listTrades(request, tradingstrat_id):
    trades = Trades.objects.filter(strategy=tradingstrat_id)
    contexto = {"trades": trades,"tradingstrat_id":tradingstrat_id}
    return render(request, "AppInvest/list_trades.html", contexto)


@login_required
def trades(request,tradingstrat_id):
    
    if request.method == 'POST':
        miFormulario = TradeForm(request.POST)
        # aquí mellega toda la información del html
        print(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data
            tradingstrat = TradingStrategies.objects.get(id=tradingstrat_id)
            print("informacion")
            print(informacion)
            # Falta Traer el foreign key
            trade = Trades(strategy=tradingstrat,time=informacion['time'], asset=informacion['asset'], tradeDirection=informacion['tradeDirection'],
                           typeentry=informacion['typeentry'], volume=informacion['volume'], 
                           price=informacion['price'],
                           stopPrice=informacion['stopPrice'], tpPrice=informacion['tpPrice'], 
                           comission=informacion['comission'], fee=informacion['fee'], 
                           swap=informacion['swap'],profit=informacion['profit'],
                           balance=informacion['balance'], comment=informacion['comment'])
            trade.save()

            trades = Trades.objects.filter(strategy=tradingstrat_id)
            # Vuelvo al inicio o a donde quieran
            contexto = {"trade": trades, "miFormulario": miFormulario,"tradingstrat_id":tradingstrat_id}
            return render(request, "AppInvest/list_trades.html",contexto)
    else:
        print("NOVALID FORM")
        miFormulario = TradeForm()  # Formulario vacio para construir el html
    return render(request, "AppInvest/trades.html", {"miFormulario": miFormulario})


@login_required
def eliminarTrades(request, trade_id,tradingstrat_id):
    #trader = Traders.objects.get(idTrader=trader_id)
    trade = Trades.objects.get(id=trade_id)
    trade.delete()
    # vuelvo al menú
    trades = Trades.objects.filter(strategy=tradingstrat_id)
    contexto = {"trades": trades,"tradingstrat_id":tradingstrat_id}
    return render(request, "AppInvest/list_trades.html", contexto)


@login_required
def editarTrades(request, trade_id,tradingstrat_id):
    # Recibe el nombre del profesor que vamos a modificar
    #trader = Traders.objects.get(idTrader=trader_id)
    trade = Trades.objects.get(id=trade_id)
    tradingstrat = TradingStrategies.objects.get(id=tradingstrat_id)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = TradeForm(request.POST)
        print("ERRORES FORM")
        print(miFormulario.errors)
        # print(miFormulario)
        if miFormulario.is_valid():  # Si pasó la validación de Django
            print(miFormulario)
            informacion = miFormulario.cleaned_data
            trade.time = informacion['time']
            trade.asset = informacion['asset']
            trade.tradeDirection = informacion['tradeDirection']
            trade.strategy = tradingstrat
            trade.typeentry = informacion['typeentry']
            trade.volume = informacion['volume']
            trade.price = informacion['price']
            trade.stopPrice = informacion['stopPrice']
            trade.tpPrice = informacion['tpPrice']
            trade.comission = informacion['comission']
            trade.fee = informacion['fee']
            trade.swap = informacion['swap']
            trade.profit = informacion['profit']
            trade.balance = informacion['balance']
            trade.comment = informacion['comment']
            trade.save()
            # Vuelvo al inicio o a donde quieran
            trades = Trades.objects.filter(strategy=tradingstrat_id)
            contexto = {"trades": trades,"tradingstrat_id":tradingstrat_id}
            return render(request, "AppInvest/list_trades.html", contexto)
        # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        # miFormulario = TradersForm(initial={'idTrader': trader.idTrader,'nombre': trader.nombre, 'apellido': trader.apellido,
        #                      'email': trader.email})
        print("ERRORES FORM")
        trade = Trades.objects.get(id=trade_id)
        miFormulario = {'time': trade.time, 'asset': trade.asset, 'tradeDirection':trade.tradeDirection ,
                        'strategy': tradingstrat,'typeentry': trade.typeentry,'volume': trade.volume,
                        'price': trade.price,'stopPrice': trade.stopPrice,'tpPrice': trade.tpPrice,
                        'comission': trade.comission,'fee': trade.fee,'swap': trade.swap,
                        'profit': trade.profit,'balance': trade.balance,'comment': trade.comment}
    # Voy al html que me permite editar
    return render(request, "AppInvest/editartrade.html", {"miFormulario": miFormulario, "id": trade_id})

def TradesUpload(request,tradingstrat_id):
    tradingstrat = TradingStrategies.objects.get(id=tradingstrat_id)
    if request.method == 'POST':
        if request.FILES['tradesFile'].content_type != 'application/vnd.ms-excel':
            messages.error(
                request, 'Archivo invalido.', extra_tags='danger')
        else:
            paramFile = io.TextIOWrapper(request.FILES['tradesFile'].file)
            portfolio1 = csv.DictReader(paramFile)
            list_of_dict = list(portfolio1)
            
            objs = [
                Trades(
                strategy=tradingstrat,
                time=row['time'], asset=row['asset'], tradeDirection=row['tradeDirection'],
                typeentry=row['typeentry'], volume=row['volume'], 
                price=row['price'],
                stopPrice=row['stopPrice'], tpPrice=row['tpPrice'], 
                comission=row['comission'], fee=row['fee'], 
                swap=row['swap'],profit=row['profit'],
                balance=row['balance'], comment=row['comment']    
                )
                for row in list_of_dict
            ]
            try:
                msg = Trades.objects.bulk_create(objs)
                returnmsg = {"status_code": 200}
                print('imported successfully')
            except Exception as e:
                print('Error While Importing Data: ',e)
                returnmsg = {"status_code": 500}
            trades = Trades.objects.filter(strategy=tradingstrat_id)
            contexto = {"trades": trades,"tradingstrat_id":tradingstrat_id}
            return render(request, "AppInvest/list_trades.html", contexto)
    contexto = {"tradingstrat_id":tradingstrat_id}    
    return render(request, "AppInvest/importtrades.html", contexto)

    


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
            tradingstrats = TradingStrategies.objects.filter(trader=request.user.id)
            contexto = {"tradingstrat": tradingstrats}
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppInvest/list_trading_strat.html", contexto)
    else:
        miFormulario = TradingStrategyForm()  # Formulario vacio para construir el html
    return render(request, "AppInvest/tradingstrategies.html", {"miFormulario": miFormulario})

# LOGIN y REGISTRO

# Vista de login


def login_request(request):

    redirect_to = request.GET.get('next', '')
    if request.user.is_authenticated:
        return HttpResponseRedirect("/", locals())

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
                        return HttpResponseRedirect(redirect_to, {"mensaje": f"Bienvenido {usuario}"})
                    else:
                        return HttpResponseRedirect("/", locals(), {"mensaje": f"Bienvenido {usuario}"})
                    # return HttpResponseRedirect("/",locals())
                    # return render(request, "AppInvest/inicio.html", {"mensaje": f"Bienvenido {usuario}"})
        else:
            # form.add_error(None, 'Usuario y/o Contraseña incorrecta')#agrega mensaje
            pass
    else:
        form = AuthenticationForm()

    return render(request, "AppInvest/login.html", {"form": form})


def logout_request(request):
    logout(request)
    return HttpResponseRedirect("/", locals())


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/", locals())

    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return HttpResponseRedirect("login", locals())

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
        avatar_form  = UploadImageForm(request.POST,request.FILES)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            messages.success(
                request, 'Datos de perfil actualizados.', extra_tags='success')
        else:
            messages.error(
                request, 'Ocurrio un error al actualizar datos de perfil.', extra_tags='danger')

        
        if avatar_form.is_valid():
            usr = User.objects.get(username=request.user)
            if Avatar.objects.filter(user=usr).exists():
                Avatar.objects.get(user=usr).delete()
            avatar = Avatar(user=usr,avatar=avatar_form.cleaned_data['avatar'])
            avatar.save()
            messages.success(
                request, 'Avatar actualizado.', extra_tags='success')

        return render(request, "AppInvest/editarPerfil.html")
    else:
        miFormulario = UserEditForm(initial={'email': usuario.email})
    return render(request, "AppInvest/editarPerfil.html", {"form": miFormulario, "usuario": usuario})

# Vista de editar el perfil
@login_required
def changePassword(request):
    usuario = request.user
    redirect_to = request.GET.get('next', '')
    
    if request.method == 'POST':
        form = UserEditPass(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            user_pass = User.objects.get(username=request.user)
            user_pass.set_password(informacion['password1'])
            user_pass.save()
            messages.success(
                request, 'Contraseña actualizada.', extra_tags='success')
            if redirect_to:
                return HttpResponseRedirect(redirect_to, {"mensaje": f"Bienvenido {usuario}"})
            else:
                return HttpResponseRedirect("editarPerfil", locals())
        else:
            messages.error(
                request, 'Ocurrio un error al actualizar contraseña.', extra_tags='danger')

        
    else:
        form = UserEditPass(initial={'email': usuario.email})
    return render(request, "AppInvest/changePass.html", {"form": form, "usuario": usuario})