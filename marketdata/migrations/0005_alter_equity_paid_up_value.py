# Generated by Django 4.0.3 on 2022-03-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketdata', '0004_equity_id_alter_equity_isin_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equity',
            name='paid_up_value',
            field=models.FloatField(verbose_name='PAID UP VALUE'),
        ),
    ]
