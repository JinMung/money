from django.shortcuts import render
from .models import Money
# Create your views here.

def all_money(request):    
    return render(request, 'home.html')

def create(request):
    money = Money()
    money.name = request.GET['name']
    money.deposit = request.GET['deposit']
    money.withdraw = request.GET['withdraw']
    money.save()
    
    #moneys = Money.objects.all()

    return render(request, 'submit.html')

def sums(request):
    moneys = Money.objects.all()    
    return render(request, 'sum.html', {'moneys' : moneys})
        