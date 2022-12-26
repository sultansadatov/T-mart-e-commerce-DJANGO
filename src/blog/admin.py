from django.contrib import admin
from datetime import date
from .models import Comments, Blog, Tags, Media

# Register your models here.

admin.site.register(Comments)
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Media)
