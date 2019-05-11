from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from accounts.models import ProfileUser
from questions.models import Questions


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