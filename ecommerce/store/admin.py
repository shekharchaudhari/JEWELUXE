from django.contrib import admin
from .models import Category, Product, Order,OrderItem

# Register your models here.



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    inlines = [OrderItemInline]

    
admin.site.register(Order, OrderAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(OrderItem)