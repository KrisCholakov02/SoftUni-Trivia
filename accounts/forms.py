from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import ProfileUser


# form that allows the user to change his/her information
class EditProfileUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    profile_picture = forms.URLField(widget=forms.URLInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))

    class Meta:
        model = ProfileUser
        fields = (
            'first_name',
            'last_name',
            'profile_picture',
            'description',
            'city',
        )
