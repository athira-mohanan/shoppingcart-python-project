from django.contrib import admin
from . models import Category,Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name','cat_slug']
    prepopulated_fields = {'cat_slug':('cat_name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name','prod_price','prod_stock','prod_available','created_on','updated_on']
    list_editable = ['prod_price','prod_stock','prod_available']
    prepopulated_fields = {'prod_slug':('prod_name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)
