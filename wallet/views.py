import re
from urllib.request import Request
from django.shortcuts import render
from .forms import AccountForm, CardForm, CurrencyForm, CustomerRegistrationForm, LoanForm, NotificationsForm, ReceiptForm, RewardForm, ThirdPartyForm, TransactionForm, WalletForm
from .models import Account, Card, Currency, Customer, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, Wallet
# Create your views here.
def register_customer(request):
    if request.method=="POST":
       form=CustomerRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
    else:
           form=CustomerRegistrationForm()    
    return render (request,"register_customer.html",{"form":form})


def list_customer(request):
    customers=Customer.objects.all()
    return render(request,"customer_list.html",{"customers":customers})


def wallet(request):
    if request.method=="POST":
        form=WalletForm(request.POST)
        if form.is_valid():
            form.save()
        else:
           form=WalletForm()  
        return render(request,"wallet.html",{"form":form})  

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet_list.html",{"wallets":wallets})        


def my_currency(request):
    if request.method=="POST":
        form=CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
        else:    
            form=CurrencyForm()
    return render (request,"currency.html",{"form":form})


def list_currency(request):
    currencies=Currency.objects.all()
    return render(request,"currency_list.html",{"currencies":currencies})


def my_account(request):
    if request.method=="POST":
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=AccountForm()
    return render (request,"account.html",{"form":form})

def list_account(request):
    accounts=Account.objects.all()
    return render(request,"account_list.html",{"accounts":accounts})

def transaction(request):
    if request.method=="POST":
        form=TransactionForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=TransactionForm()
    return render (request,"transaction.html",{"form":form})    

def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"transaction_list.html",{"transactions":transactions})

def my_card(request):
    if request.method=="POST":
        form=CardForm(request.POST)
        if form.is_valid():
            form.save()
        else:
           form=CardForm()
    return render (request,"card.html",{"form":form})   

def list_card(request):
    cards=Card.objects.all() 
    return render(request,"card_list.html",{"cards":cards})    

def third_party(request):
    if request.method=="POST":
        form=ThirdPartyForm(request.POST)
        if form.is_valid():
            form.save()
        else:    
            form=ThirdPartyForm()
    return render (request,"thirdparty.html",{"form":form})  

def list_thirdparty(request):
    thirdparties=ThirdParty.objects.all()
    return render(request,"thirdparty_list.html",{"thirdparties":thirdparties})


def notifications(request): 
    if request.method=="POST":
        form=NotificationsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
         form=NotificationsForm()
    return render (request,"notifications.html",{"form":form}) 


def list_notifications(request):
    notifications=Notifications.objects.all()
    return render(request,"notifications_list.html",{"notifications":notifications})


def receipt(request)   :
     if request.method=="POST":
        form=ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
        else:   
            form=ReceiptForm()  
     return render (request,"receipt.html",{"form":form})    
     
def list_receipt(request):
    receipts=Receipt.objects.all()  
    return render(request,"receipt_list.html",{"receipts":receipts})  

         


def loan(request)   :
    if request.method=="POST":
        form=LoanForm(request.POST)
        if form.is_valid():
            form.save()
        else:   
           form=LoanForm()
    return render (request,"loan.html",{"form":form}) 

def list_loan(request):
    loans=Loan.objects.all()  
    return render(request,"loan_list.html",{"loans":loans})  

    


def reward(request):
    if request.method=="POST":
        form=RewardForm(request.POST)
        if form.is_valid():
            form.save()
        else:   
         form=RewardForm()
    return render(request,"reward.html",{"form":form})    

def list_reward(request):
    rewards=Reward.objects.all()  
    return render(request,"reward_list.html",{"rewards":rewards})      