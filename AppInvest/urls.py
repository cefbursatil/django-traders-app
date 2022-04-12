from django.urls import path

from AppInvest import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio , name="Inicio"), #esta era nuestra primer view
    path('trades', views.trades, name="Trades"),
    path('tradingstrategiesadd', views.tradingstrategies, name="TradingStrategiesAdd"),
    path('Traders', views.traders, name="Traders"),
    path('Usuarios', views.listTraders, name="Usuarios"),
    path('eliminarTrader/<trader_id>/', views.eliminarTrader, name="EliminarTrader"),
    path('editarTrader/<trader_id>/', views.editarTrader, name="EditarTrader"),
    path('eliminarTradingStrat/<tradingstrat_id>/', views.eliminarTradingStrat, name="EliminarTradingStrat"),
    path('editarTraderStrat/<tradingstrat_id>/', views.editarTradingStrat, name="EditarTradingStrat"),
    path('tradingstrategies', views.listTradingStrategies, name="TradingStrategies"),
    path('trades/<tradingstrat_id>/', views.listTrades, name="TradesList"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppInvest/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
]