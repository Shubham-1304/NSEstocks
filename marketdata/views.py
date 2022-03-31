from django.http import HttpResponse
import datetime
from django.shortcuts import render
import csv
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from .models import Equity,AllReports
from .serializers import EquitySerializer,AllReportsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import Details
import requests


fs=FileSystemStorage(location='temp/')

def enterdata(request):
    file = open('C:/Users/shubh/Python vs/stocks/EQUITY_L.csv')
    #file='C:/Users/shubh/Python vs/stocks/EQUITY_L.csv'
    content=file.read()
    file_content=ContentFile(content)
    file_name=fs.save(
        "_tmp.csv",file_content
    )
    tmp_file=fs.path(file_name)
    csv_file=open(tmp_file,errors="ignore")
    reader=csv.reader(csv_file)
    next(reader)
    lst=[]
    i=1
    for row in reader:
        (symbol,name_of_company,series,date_of_listing,paid_up_value,
        market_value,isin_number,face_value)=row
        id=i
        lst.append(Equity(id,symbol,name_of_company,series,date_of_listing,paid_up_value,
        market_value,isin_number,face_value))
        i+=1
    Equity.objects.bulk_create(lst)
    return HttpResponse("file saved")

def allreports(request):
    file = open('C:/Users/shubh/Python vs/stocks/cm31MAR2022bhav.csv')
    content=file.read()
    file_content=ContentFile(content)
    file_name=fs.save(
        "_tmp2.csv",file_content
    )
    tmp_file=fs.path(file_name)
    csv_file=open(tmp_file,errors="ignore")
    reader=csv.reader(csv_file)
    next(reader)
    lst=[]
    i=1
    for row in reader:
        print(row)
        (symbol,series,openn,high,low,close,last,prevclose,tottrdqty,tottrdval,timestamp,totaltrades,isin,x)=row
        id=i
        timestamp=datetime.datetime.strptime(timestamp, "%d-%b-%Y").strftime("%Y-%m-%d")
        lst.append(AllReports(id,symbol,series,openn,high,low,close,last,prevclose,tottrdqty,tottrdval,timestamp,totaltrades,isin))
        i+=1
    AllReports.objects.bulk_create(lst)
    return HttpResponse("file saved")

@api_view(['GET'])
def getData(request):
    try:
        data=request.data
        symbol=Equity.objects.filter(symbol=data['symbol'])
        serializer=EquitySerializer(symbol,many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        Response(e)

def detailsOfSymbol(request):
    form=Details()
    if request.method=='POST':
        form=Details(request.POST)
        if form.is_valid():
            symbol= form.cleaned_data['symbol']
            print(symbol)
        r = requests.get(f'http://127.0.0.1:8000/equity/getdata/',)
        print(r)
        if r.status_code == 200:
            return HttpResponse('Successful')
        else:
            return HttpResponse('UnSuccessful')
    context={'form':form}
    return render(request,'detail_form.html',context)



