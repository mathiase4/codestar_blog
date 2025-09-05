from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):
    def test_form_is_valid(self):
        """Test for all fields"""
        form = CollaborateForm({
            "name": "Mathias",
            "email": "test@test.com",
            "message": "Hello!"
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = CollaborateForm({
            "name": "",
            "email": "test@test.com",
            "message": "Hello!"
        })
        self.assertFalse(form.is_valid(), msg="Name missing should make form invalid")

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = CollaborateForm({
            "name": "Matt",
            "email": "",
            "message": "Hello!"
        })
        self.assertFalse(form.is_valid(), msg="Email missing should make form invalid")

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = CollaborateForm({
            "name": "Matt",
            "email": "test@test.com",
            "message": ""
        })
        self.assertFalse(form.is_valid(), msg="Message missing should make form invalid")
