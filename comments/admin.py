from django.contrib import admin
from .models import Comment

class ListComment(admin.ModelAdmin):
    list_display = ('description','amiibo_id', 'user_id',)
    list_display_links = ('description',)
    search_fields = ('description','amiibo_id', 'user_id',)
    list_filter = ('amiibo_id', 'user_id',)
    list_per_page = 10

admin.site.register(Comment, ListComment)