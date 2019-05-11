from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response
from django.views import generic
from random import randint

from accounts.models import ProfileUser
from questions.models import Questions


def get_question(request):
    played_questions_pks = []
    while True:
        random_number = randint(0, 3)
        if random_number in played_questions_pks:
            continue
        else:
            played_questions_pks.append(random_number)
            question = Questions.objects.get(pk=2)
            return render_to_response('play_game.html', {'playing_question': question})


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
