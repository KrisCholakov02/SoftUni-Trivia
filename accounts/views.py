from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, User

from .models import ProfileUser
from .forms import EditProfileUserForm


# function that checks if the user has the rights to edit
def has_access_to_modify(current_user, profile_user):
    if current_user.is_superuser:
        return True
    elif current_user.id == profile_user.user.id:
        return True
    return False


# class that shows user's details
class UserDetail(generic.DetailView):
    model = ProfileUser
    template_name = 'profile_user.html'
    context_object_name = 'my_user'


# class for signing up in the web application
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'


# function that redirects the user after login
def redirect_user(request):
    url = f'/game/'  # home page
    return HttpResponseRedirect(url)


# class for editing user's information
class ProfileUserEdit(LoginRequiredMixin, generic.UpdateView):
    model = ProfileUser
    form_class = EditProfileUserForm
    template_name = 'question_create.html'
    success_url = '/game/'

# function for verifying the form
    def form_valid(self, form):
        author = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.author = author
        return super().form_valid(form)

# getting user's information
    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = ProfileUser.objects.get(pk=pk)
        form = EditProfileUserForm(request.POST or None, instance=instance)
        return render(request, 'question_create.html', {'form': form})
