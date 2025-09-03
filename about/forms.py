from .models import CollaborateRequest
from django import forms

class CollaborateForm():
   class meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
        