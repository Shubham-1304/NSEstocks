# Generated by Django 4.0.3 on 2022-03-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equity',
            name='id',
        ),
        migrations.AlterField(
            model_name='equity',
            name='symbol',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='SYMBOL'),
        ),
    ]
