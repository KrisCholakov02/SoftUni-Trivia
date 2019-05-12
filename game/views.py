from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response
from django.views import generic
import random

from accounts.models import ProfileUser
from questions.models import Questions


def get_question(request):
    played_questions_pks = []
    while True:
        random_number = random.randint(1, Questions.objects.all().filter(checked=1).count())
        if random_number in played_questions_pks:
            continue
        else:
            played_questions_pks.append(random_number)
            question = Questions.objects.get(pk=random_number)
            answers = [question.answer1, question.answer2, question.answer3, question.correct_answer]
            random.shuffle(answers)  # shuffle the answers
            return render_to_response('play_game.html', {'playing_question': question, 'answers': answers})


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
