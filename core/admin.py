from django.contrib import admin
from .models import Product, Cart, Contactus, Orders
# Register your models here.

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Contactus)
admin.site.register(Orders)
