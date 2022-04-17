from django.contrib import admin
from .models import * #importamos el archivo models
# Register your models here.
#registramos los modelos
admin.site.register(Traders)
admin.site.register(TradingStrategies)
admin.site.register(Trades)
admin.site.register(Avatar)
