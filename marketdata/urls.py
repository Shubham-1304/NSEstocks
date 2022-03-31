from django import views
from django.urls import path
from .views import enterdata,allreports,getData,detailsOfSymbol

urlpatterns=[
    path('enterdata/',enterdata,name="enterdata"),
    path('allreports/',allreports,name="allreports"),
    path('getdata/',getData,name="getdata"),
    path('detailsofsymbol/',detailsOfSymbol,name="detailsofsymbol"),
]