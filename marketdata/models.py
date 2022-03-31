from email.utils import format_datetime
from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

class Equity(models.Model):
    id=models.AutoField(primary_key=True)
    symbol=models.CharField(_("SYMBOL"),max_length=255)
    name_of_company=models.CharField(_("NAME OF COMPANY"),max_length=255)
    series=models.CharField(_("SERIES"),max_length=255)
    date_of_listing=models.CharField(_("DATE OF LISTING"),max_length=255)
    paid_up_value=models.FloatField(_("PAID UP VALUE"))
    market_value=models.IntegerField(_("MARKET VALUE"))
    isin_number=models.CharField(_("ISIN NUMBER"),max_length=255,)
    face_value=models.IntegerField(_("FACE VALUE"))

class AllReports(models.Model):
    id=models.AutoField(primary_key=True)
    symbol=models.CharField(_("SYMBOL"),max_length=255)
    series=models.CharField(_("SERIES"),max_length=255)
    open=models.FloatField(_("OPEN"))
    high=models.FloatField(_("HIGH"))
    low=models.FloatField(_("LOW"))
    close=models.FloatField(_("CLOSE"))
    last=models.FloatField(_("LAST"))
    prevclose=models.FloatField(_("PREVCLOSE"))
    tottrdqty=models.FloatField(_("TOTTRDQTY"))
    tottrdval=models.CharField(_("TOTTRDVAL"),max_length=255)
    timestamp=models.DateField(_("TIMESTAMP"),default="########")
    totaltrades=models.IntegerField(_("TOTALTRADES"),default=0)
    isin=models.CharField(_("ISIN"),max_length=255)









# Create your models here.
