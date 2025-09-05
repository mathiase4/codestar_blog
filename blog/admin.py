from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model.
    Defines list display, filters, search, slug generation,
    ordering, and Summernote editor for content.
    """ 
    
    list_display = ("title", "author", "status", "created_on")
    list_filter = ("status", "created_on", "author")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_on",)
    summernote_fields = ('content',)
    

# Register your models here.
admin.site.register(Comment)