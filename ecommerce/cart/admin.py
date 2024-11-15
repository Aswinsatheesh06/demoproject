from django.contrib import admin
from cart.models import Payment
from cart.models import Order_details
from cart.models import Cart
# Register your models here.
admin.site.register(Cart)

admin.site.register(Payment)
admin.site.register(Order_details)
