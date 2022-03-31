from django.forms import ModelForm
from .models import Equity,AllReports

class Details(ModelForm):
    class Meta:
        model=Equity
        fields=['symbol']