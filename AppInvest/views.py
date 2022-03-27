from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppInvest.models import Trades, TradingStrategies,Traders
from AppInvest.forms import TradeForm, TradingStrategyForm,TradersForm

def inicio(request):

      return render(request, "AppInvest/inicio.html")


###TRADERS
def traders(request):
      traders = Traders.objects.all()
      #trae todos los profesores
      if request.method == 'POST':
            miFormulario = TradersForm(request.POST) 
            #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid: 
                  #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  trader = Traders(idTrader=informacion['idTrader'], nombre=informacion['nombre'],apellido=informacion['apellido'], email=informacion['email'])
                  trader.save()
                  return render(request, "AppInvest/inicio.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario= TradersForm() #Formulario vacio para construir el html
      contexto= {"traders":traders,"miFormulario":miFormulario}  
      return render(request, "AppInvest/traders.html", contexto)

def eliminarTrader(request, trader_id):
      #trader = Traders.objects.get(idTrader=trader_id)
      trader = Traders.objects.get(id=trader_id)
      trader.delete()
      # vuelvo al menú
      traders = Traders.objects.all() # trae todos los profesores
      contexto = {"traders": traders}
      return render(request, "AppInvest/traders.html", contexto)

def editarTrader(request, trader_id):
  # Recibe el nombre del profesor que vamos a modificar
  #trader = Traders.objects.get(idTrader=trader_id)
  trader = Traders.objects.get(id=trader_id)
  # Si es metodo POST hago lo mismo que el agregar
  if request.method == 'POST':
    # aquí mellega toda la información del html
    miFormulario = TradersForm(request.POST)
    
    #print(miFormulario)
    if miFormulario.is_valid: # Si pasó la validación de Django
      print(miFormulario)
      informacion = miFormulario.cleaned_data
      trader.nombre = informacion['nombre']
      trader.apellido = informacion['apellido']
      trader.email = informacion['email']
      trader.save()
      # Vuelvo al inicio o a donde quieran
      return render(request, "AppInvest/inicio.html")
  # En caso que no sea post
  else:
    # Creo el formulario con los datos que voy a modificar
    #miFormulario = TradersForm(initial={'idTrader': trader.idTrader,'nombre': trader.nombre, 'apellido': trader.apellido,
    #                      'email': trader.email})
    miFormulario = {'idTrader': trader.idTrader,'nombre': trader.nombre, 'apellido': trader.apellido,
                          'email': trader.email}
  # Voy al html que me permite editar
  return render(request, "AppInvest/editartrader.html", {"miFormulario": miFormulario, "id": trader_id})

#################################################

def trades(request):
      
      if request.method == 'POST':
            miFormulario = TradeForm(request.POST) 
            #aquí mellega toda la información del html
            print(request.POST)
            print(miFormulario)
            if miFormulario.is_valid: 
                  #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  #Falta Traer el foreign key
                  trade = Trades (idTrade=informacion['idTrade'], activo=informacion['activo'],tradeDirection=informacion['tradeDirection'], typeentry=informacion['typeentry'],precio=informacion['precio'], descripcion=informacion['descripcion'])
                  trade.save()
                  return render(request, "AppInvest/inicio.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario= TradeForm() #Formulario vacio para construir el html
      return render(request, "AppInvest/trades.html", {"miFormulario":miFormulario})





def tradingstrategies(request):
      if request.method == 'POST':
            miFormulario = TradingStrategyForm(request.POST) 
            #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid: 
                  #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  #Falta Traer el foreign key
                  tradingstrat = TradingStrategies (idStrategy=informacion['idStrategy'], nombre=informacion['nombre'],activo=informacion['activo'], descripcion=informacion['descripcion'])
                  tradingstrat.save()
                  return render(request, "AppInvest/inicio.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario= TradingStrategyForm() #Formulario vacio para construir el html
      return render(request, "AppInvest/tradingstrategies.html", {"miFormulario":miFormulario})