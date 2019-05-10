from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import ProfileUser


class UserDetail(generic.DetailView):
    model = ProfileUser
    template_name = 'profile_user.html'
    context_object_name = 'user'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'


def redirect_user(request):
    url = f'/game/'
    return HttpResponseRedirect(url)
