# Generated by Django 4.0.3 on 2022-04-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppInvest', '0009_rename_activo_trades_asset_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='trades',
            name='profit',
            field=models.FloatField(default=0),
        ),
    ]
