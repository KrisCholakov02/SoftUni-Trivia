from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import ProfileUser


class EditProfileUserForm(UserChangeForm):
    template_name = 'questions/templates/question_create.html'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'profile_picture',
            'description',
            'city',

        )
