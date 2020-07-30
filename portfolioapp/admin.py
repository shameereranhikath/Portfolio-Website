from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.site_header='Portfolio Admin'
admin.site.site_title='Portfolio Admin Area'
admin.site.index_title='Welcome to Portfolio Admin Area'

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone')

admin.site.register(Contact,ContactAdmin)

