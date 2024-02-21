from django.contrib import admin
from .models import post , comments


class postAdmin(admin.ModelAdmin):
    list_display = ('id','title','date')

class commentsAdmin(admin.ModelAdmin):
    list_display = ('cum_id','text')


admin.site.register(post,postAdmin)
admin.site.register(comments,commentsAdmin)