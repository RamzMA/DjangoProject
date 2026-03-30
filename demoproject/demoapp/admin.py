from django.contrib import admin
from .models import Menu, MenuCategory, ApplicationForm

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(ApplicationForm)