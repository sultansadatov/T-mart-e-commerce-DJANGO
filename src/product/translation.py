from .models import Product, Category
from modeltranslation.translator import TranslationOptions, register

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("product_name", "product_info", "product_description", "product_detail", "delivery_info",)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title",)