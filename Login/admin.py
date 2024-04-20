from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, PostComment

class PostAdmin(SummernoteModelAdmin):
    list_display = ('body',)
    list_filter = ('body',)
    search_fields =['intro']
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
admin.site.register(PostComment)