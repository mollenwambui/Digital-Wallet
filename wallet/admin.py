from django.contrib import admin
# Register your models here.
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notifications
from .models import Receipt
from .models import Reward
from .models import Loan

 
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","adress")
    search_fields = ("first_name","last_name")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("balance","date_created","pin")
    search_fields = ("balance","pin")

admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
     list_display=("balance","account_name")
     search_fields = ("balance","account_name")

admin.site.register(Account,AccountAdmin)  

class TransactionAdmin(admin.ModelAdmin):
      list_display=("transaction_code","transaction_amount","transaction_type")
      search_fields = ("transaction_code","transaction_amount","transaction_type")

admin.site.register(Transaction,TransactionAdmin) 

class  CardAdmin(admin.ModelAdmin):
       list_display=("card_number","card_name","date_issued")
       search_fields = ("card_number","card_name","date_issued")

admin.site.register(Card,CardAdmin)    

class ThirdpartyAdmin(admin.ModelAdmin):
      list_display=("name","currency","transaction_cost")
      search_fields =("name","currency","transaction_cost")

admin.site.register(ThirdParty,ThirdpartyAdmin)   

class NotificationsAdmin(admin.ModelAdmin):
      list_display=("description","title","status")
      search_fields=("description","title","status")

admin.site.register(Notifications,NotificationsAdmin)  

class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_type","bill_number","receipt_file")
    search_fields=("receipt_type","bill_number","receipt_file")

admin.site.register(Receipt,ReceiptAdmin)    

class LoanAdmin(admin.ModelAdmin):
      list_display=("loan_id","purpose","amount","name")
      search_fields=("loan_id","purpose","amount","name")

admin.site.register(Loan,LoanAdmin)      


class RewardAdmin(admin.ModelAdmin):
    list_display=("date_of_reward","points","transaction")
    search_fields=("date_of_reward","points","transaction")


admin.site.register(Reward,RewardAdmin)





