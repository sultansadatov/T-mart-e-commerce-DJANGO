from datetime import date
from django.contrib import admin

from .models import Product, Size, Color, Category,  Reviews, Brand, Cart, Media
from modeltranslation.admin import TranslationAdmin


from modeltranslation.admin import TranslationAdmin

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    search_fields = [ 'product_name', 'product_description',]
    list_display = ['product_name', 'product_description']
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


# admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(Media)
