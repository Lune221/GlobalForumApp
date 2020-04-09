from django.contrib import admin

# Register your models here.
from .models import *

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('Title','Pub_User')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('Content', 'Subject_Id', 'Comment_User')

admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
