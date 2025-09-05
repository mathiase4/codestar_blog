from .models import CollaborateRequest
from django import forms

class CollaborateForm():
   """
    Form for submitting collaboration requests.
    Includes name, email, and message fields linked to the CollaborateRequest model.
    """
   class meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
        