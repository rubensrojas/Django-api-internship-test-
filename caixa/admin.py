from django.contrib import admin
# local
from .models import Product
from account.models import Account
# Register your models here.

admin.site.register(Product)
admin.site.register(Account)