from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Questions, Level
from .forms import CreateQuestionForm, LevelForm

from accounts.models import ProfileUser


def has_access_to_modify(current_user, furniture):
    if current_user.is_superuser:
        return True
    elif current_user.id == furniture.user.id:
        return True
    return False


class UserQuestionsList(LoginRequiredMixin, generic.ListView):
    model = Questions
    template_name = 'questions_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        author_id = int(self.request.user.id)

        try:
            author = ProfileUser.objects.all().filter(user__pk=author_id)[0]
            questions = Questions.objects.all().filter(author=author.pk)
            return questions
        except:
            return []


class QuestionCreate(LoginRequiredMixin, generic.CreateView):
    model = Questions
    template_name = 'question_create.html'
    form_class = CreateQuestionForm
    success_url = '/questions/mine/'

    def form_valid(self, form):
        author = ProfileUser.objects.all().filter(user__pk=self.request.user.id)[0]
        form.instance.author = author
        return super().form_valid(form)


class QuestionDelete(LoginRequiredMixin, generic.DeleteView):
    model = Questions
    login_url = 'accounts/login/'
    context_object_name = 'questions'

    def get(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        return render(request, 'question_delete.html', {'furniture': self.get_object()})

    def post(self, request, pk):
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        furniture = self.get_object()
        furniture.delete()
        return HttpResponseRedirect('/game/')


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
        if not has_access_to_modify(self.request.user, self.get_object()):
            return render(request, 'permission_denied.html')
        instance = Questions.objects.get(pk=pk)
        form = CreateQuestionForm(request.POST or None, instance=instance)
        return render(request, 'question_create.html', {'form': form})


class QuestionDetail(LoginRequiredMixin, generic.DetailView):
    model = Questions
    login_url = '/accounts/login/'
    context_object_name = 'question'
    template_name = 'question_detail.html'
