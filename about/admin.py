from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import about


# Register your models here.

admin.site.register(about)

class AboutAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('content',)

