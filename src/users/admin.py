from django.contrib import admin
from .models import User, Wishlist


admin.site.register(Wishlist)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email']

