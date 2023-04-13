from django.shortcuts import render
from yahoo_fin.stock_info import *
from django.http import HttpResponse
# Create your views here.

def stock_picker(request):
    stock_picker=tickers_nifty50()
    return render(request,'mainapp/stockpicker.html',{'stockpicker':stock_picker})

def stock_tracker(request):
    stockpicker=request.GET.getlist('stockpicker')
    print(stockpicker)
    available_stocks=tickers_nifty50()
    data={}
    for i in stockpicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
    for i in stockpicker:
        details=get_quote_table(i)
        data.update({i:details})
        
    print(data)
    return render(request,'mainapp/stocktracker.html')