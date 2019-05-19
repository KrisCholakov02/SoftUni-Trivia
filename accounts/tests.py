from django.test import TestCase
from django.test import Client
from .forms import *
from django.contrib.auth.forms import UserCreationForm


class SetupClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="user@mp.com", password="user", first_name="user", phone=12345678)


class UserFormTest(TestCase):
    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserCreationForm(data={'username': "valid", 'password1': "valid12345", 'password2': "valid12345"})
        self.assertTrue(form.save())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = UserCreationForm(data={'username': "invalid", 'password1': "valid12345", 'password2': "invalid12345"})
        self.assertTrue(form.save())