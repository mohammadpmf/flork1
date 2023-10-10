from django.contrib import admin

from .models import BPost

class BPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status' , 'datetime_created', 'datetime_modified', 'author']
    
admin.site.register(BPost, BPostAdmin)
