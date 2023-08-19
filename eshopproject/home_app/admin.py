from django.contrib import admin
from .models import *

# Register your models here.
class cat_admin(admin.ModelAdmin):
    list_display = ('pk','name','slug',)


    prepopulated_fields = {'slug':('name',)}


admin.site.register(Category,cat_admin)


class pro_admin(admin.ModelAdmin):
    list_display = ('pk','name','slug','category','price', 'img','desc','stock','available',)
    list_editable = ('price','stock','img','name')
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Product,pro_admin)