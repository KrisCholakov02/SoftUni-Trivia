from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response
from django.views import generic
import random

from accounts.models import ProfileUser
from questions.models import Questions


class GameTactics():
    def fifty_fifty(request, pk):
        question = Questions.objects.get(pk=pk)
        correct_answer = question.correct_answer
        answers = [question.answer1, question.answer2, question.answer3]
        random_number = random.randint(0, 2)
        other_answer = answers[random_number]
        f_answers = [correct_answer, other_answer]
        random.shuffle(f_answers)
        return render_to_response('play_game.html', {'playing_question': question, 'answers': f_answers})

    def right_one(request, pk):
        question = Questions.objects.get(pk=pk)
        correct_answer = question.correct_answer
        answers = [correct_answer]
        return render_to_response('play_game.html', {'playing_question': question, 'answers': answers})

    def remove_one(request, pk):
        question = Questions.objects.get(pk=pk)
        correct_answer = question.correct_answer
        answers = [question.answer1, question.answer2, question.answer3]
        random.shuffle(answers)
        answers.remove(answers[2])
        answers.append(correct_answer)
        random.shuffle(answers)
        return render_to_response('play_game.html', {'playing_question': question, 'answers': answers})

    def start_game(request):
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
