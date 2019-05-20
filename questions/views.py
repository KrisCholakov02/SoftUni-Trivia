from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Questions, Level
from .forms import CreateQuestionForm, LevelForm

from accounts.models import ProfileUser


# function that checks if the user have the rights to modify
def has_access_to_modify(current_user, questions):
    if current_user.is_superuser:
        return True
    elif current_user.id == questions.author.id:
        return True
    return False


# getting user's questions
class UserQuestionsList(LoginRequiredMixin, generic.ListView):
    model = Questions
    template_name = 'questions_list.html'
    context_object_name = 'questions'

# function that gets only user's questions
    def get_queryset(self):
        if self.request.user.is_superuser:  # if the user is admin show all questions
            try:
                questions = Questions.objects.all() # getting all questions
                return questions
            except:
                return []
        else:
            author_id = int(self.request.user.id)  # getting user's pk
            try:
                author = ProfileUser.objects.all().filter(user__pk=author_id)[0]  # getting user by pk
                questions = Questions.objects.all().filter(author=author.pk)  # getting only user's questions
                return questions
            except:
                return []


# class that allows creation of questions by all authenticated users
class QuestionCreate(LoginRequiredMixin, generic.CreateView):
    model = Questions
    template_name = 'question_create.html'
    form_class = CreateQuestionForm
    success_url = '/questions/mine/'

    def form_valid(self, form):
        author = ProfileUser.objects.get(user__pk=self.request.user.id)
        form.instance.author = author
        return super().form_valid(form)


# class that allows the deletion of questions by all authenticated users
class QuestionDelete(LoginRequiredMixin, generic.DeleteView):
    model = Questions
    login_url = 'accounts/login/'
    context_object_name = 'questions'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'question_delete.html', {'question': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        question = self.get_object()
        question.delete()
        return HttpResponseRedirect('/game/')


# class that allows editing of questions by all authenticated users
class QuestionEdit(LoginRequiredMixin, generic.UpdateView):
    model = Questions
    form_class = CreateQuestionForm
    template_name = 'question_create.html'
    success_url = '/game/'

    def form_valid(self, form):
        author = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.author = author
        return super().form_valid(form)

    def get(self, request, pk):
        # checking if the user has rights to modify
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Questions.objects.get(pk=pk)
        form = CreateQuestionForm(request.POST or None, instance=instance)
        return render(request, 'question_create.html', {'form': form})


# class that shows question's details
class QuestionDetail(LoginRequiredMixin, generic.DetailView):
    model = Questions
    login_url = '/accounts/login/'
    context_object_name = 'question'
    template_name = 'question_detail.html'
