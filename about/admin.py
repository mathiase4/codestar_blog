from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import about as About


# Register your models here.

admin.site.register(About)

class AboutAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content',)

