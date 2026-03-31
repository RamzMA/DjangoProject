from django.contrib import admin
from .models import Menu, MenuCategory, ApplicationForm, Person
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)
admin.site.register(Person)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith", )

@admin.register(User)
class NewAdmin(UserAdmin):
    def get_form(self, request, obj, **kwargs):
        form = super().get_form(request, obj, **kwargs)
    
        is_supervisor = request.user.is_superuser

        if not is_supervisor:
            form.base_fields['username'].disabled = True

        return form



# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(ApplicationForm)