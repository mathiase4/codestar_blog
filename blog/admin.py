from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    list_filter = ("status", "created_on", "author")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_on",)


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)