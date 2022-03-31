from rest_framework import serializers
from .models import Equity,AllReports

class EquitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Equity
        fields='__all__'

class AllReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AllReports
        fields='__all__'