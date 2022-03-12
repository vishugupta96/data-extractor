from django.contrib import admin

from yt.models import Client,Link

# Register your models here
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id','assigned_to']

admin.site.register(Link)
         
# admin.site.register(Client)
