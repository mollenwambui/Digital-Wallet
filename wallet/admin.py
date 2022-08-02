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


admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdParty)
admin.site.register(Notifications)
admin.site.register(Receipt)
admin.site.register(Reward)
admin.site.register(Loan)






