from django.urls import path

from AppInvest import views

urlpatterns = [
   
    path('', views.inicio , name="Inicio"), #esta era nuestra primer view
    path('trades', views.trades, name="Trades"),
    path('tradingstrategies', views.tradingstrategies, name="TradingStrategies"),
    path('Traders', views.traders, name="Traders"),
    path('eliminarTrader/<trader_id>/', views.eliminarTrader, name="EliminarTrader"),
    path('editarTrader/<trader_id>/', views.editarTrader, name="EditarTrader"),
]