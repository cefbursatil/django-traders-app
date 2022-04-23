from django.urls import path

from AppInvest import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.inicio , name="Inicio"), #esta era nuestra primer view
    path('tradesadd/<tradingstrat_id>/', views.trades, name="TradesAdd"),
    path('tradingstrategiesadd', views.tradingstrategies, name="TradingStrategiesAdd"),
    path('Traders', views.traders, name="Traders"),
    path('Usuarios', views.listTraders, name="Usuarios"),
    path('eliminarTrader/<trader_id>/', views.eliminarTrader, name="EliminarTrader"),
    path('editarTrader/<trader_id>/', views.editarTrader, name="EditarTrader"),
    path('eliminarTradingStrat/<tradingstrat_id>/', views.eliminarTradingStrat, name="EliminarTradingStrat"),
    path('editarTraderStrat/<tradingstrat_id>/', views.editarTradingStrat, name="EditarTradingStrat"),
    path('eliminarTrade/<trade_id>/<tradingstrat_id>/', views.eliminarTrades, name="EliminarTrade"),
    path('editarTrade/<trade_id>/<tradingstrat_id>/', views.editarTrades, name="EditarTrade"),
    path('tradingstrategies', views.listTradingStrategies, name="TradingStrategies"),
    path('trades/<tradingstrat_id>/', views.listTrades, name="TradesList"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', views.logout_request, name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('changePassword', views.changePassword, name="ChangePassword"),
    path('importtrades/<tradingstrat_id>/', views.TradesUpload, name='importtrade')
]