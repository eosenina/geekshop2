from mainapp.models import ProductCategory, Product
from django.contrib import admin


# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    ordering = ('name',)
    search_fields = ('name',)
