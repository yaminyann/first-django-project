from django.contrib import admin
from . models import UserContactForm
# Register your models here.


# Contact Admin register
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']
admin.site.register(UserContactForm,ContactAdmin)