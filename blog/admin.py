from django.contrib import admin

from .models import BPost, Comment

class BPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status' , 'datetime_created', 'datetime_modified', 'author']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text' , 'datetime_created', 'post']

admin.site.register(BPost, BPostAdmin)
admin.site.register(Comment, CommentAdmin)
