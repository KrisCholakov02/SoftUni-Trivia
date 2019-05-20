from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response
from django.views import generic
from django.http import HttpResponse
import random

from accounts.models import ProfileUser
from questions.models import Questions, Level
from games.views import create_game


class GameTactics:
    played_questions_pks = []
    points = 0
    ff_display = True
    ra_display = True
    remove_display = True
    number_of_all_questions = 5 * Level.objects.all().count()
    questions_in_db = Questions.objects.all().filter(checked=1).count()

# This is admin method for emergency restart
    def restart_game(request):
        if request.user.is_superuser:
            GameTactics.played_questions_pks = []
            return HttpResponse('Done')
        else:
            return render_to_response('permission_denied.html')

    def fifty_fifty(request, pk):
        question = Questions.objects.get(pk=pk)
        correct_answer = question.correct_answer
        answers = [question.answer1, question.answer2, question.answer3]
        random_number = random.randint(0, 2)
        other_answer = answers[random_number]
        f_answers = [correct_answer, other_answer]
        random.shuffle(f_answers)
        GameTactics.ff_display = False
        return render_to_response('play_game.html', {'playing_question': question, 'answers': f_answers,
                                                     'user': request.user, 'points': GameTactics.points,
                                                     'ff_display': GameTactics.ff_display,
                                                     'ra_display': GameTactics.ra_display,
                                                     'remove_display': GameTactics.remove_display})

    def right_answer(request, pk):
        question = Questions.objects.get(pk=pk)
        correct_answer = question.correct_answer
        answers = [correct_answer]
        GameTactics.ra_display = False
        return render_to_response('play_game.html', {'playing_question': question, 'answers': answers,
                                                     'user': request.user, 'points': GameTactics.points,
                                                     'ff_display': GameTactics.ff_display,
                                                     'ra_display': GameTactics.ra_display,
                                                     'remove_display': GameTactics.remove_display})

    def remove_answer(request, pk):
        question = Questions.objects.get(pk=pk)
        correct_answer = question.correct_answer
        answers = [question.answer1, question.answer2, question.answer3]
        random.shuffle(answers)
        answers.remove(answers[2])
        answers.append(correct_answer)
        random.shuffle(answers)
        GameTactics.remove_display = False
        return render_to_response('play_game.html', {'playing_question': question, 'answers': answers,
                                                     'user': request.user, 'points': GameTactics.points,
                                                     'ff_display': GameTactics.ff_display,
                                                     'ra_display': GameTactics.ra_display,
                                                     'remove_display': GameTactics.remove_display})

    def start_game(request):
        GameTactics.played_questions_pks = []
        GameTactics.points = 0
        GameTactics.ff_display = True
        GameTactics.ra_display = True
        GameTactics.remove_display = True
        while True:
            random_number = random.randint(1, Questions.objects.all().filter(checked=1, level=Level.objects.get(pk=1))
                                           .count())
            if random_number in GameTactics.played_questions_pks:
                continue
            else:
                GameTactics.played_questions_pks.append(random_number)
                question = Questions.objects.get(pk=random_number)
                answers = [question.answer1, question.answer2, question.answer3, question.correct_answer]
                random.shuffle(answers)
                return render_to_response('play_game.html', {'playing_question': question, 'answers': answers,
                                                             'user': request.user, 'points': GameTactics.points,
                                                             'ff_display': GameTactics.ff_display,
                                                             'ra_display': GameTactics.ra_display,
                                                             'remove_display': GameTactics.remove_display})

    def next_question(request, pk, correct):
        question = Questions.objects.get(pk=pk)
        cnt = len(GameTactics.played_questions_pks)
        if 0 <= cnt < 5:
            level = Level.objects.get(pk=1)
        elif 5 <= cnt < 10:
            level = Level.objects.get(pk=2)
        elif 10 <= cnt < 15:
            level = Level.objects.get(pk=3)
        else:
            level = 0
        if level == 0:
            create_game(request.user, cnt, level, GameTactics.points)
            return render_to_response('end_game.html', {'points': GameTactics.points, 'user': request.user})
        elif correct == '1':
            GameTactics.points += question.level.points
            while True:
                random_number = random.randint(1, Questions.objects.all().filter(checked=1).count())
                if Questions.objects.get(pk=random_number) not in Questions.objects.all().filter(level=level):
                    continue
                if random_number in GameTactics.played_questions_pks:
                    continue
                elif len(GameTactics.played_questions_pks) == (GameTactics.questions_in_db + 1):
                    create_game(request.user, cnt, level, GameTactics.points)
                    return render_to_response('end_game.html', {'points': GameTactics.points, 'user': request.user})
                else:
                    GameTactics.played_questions_pks.append(random_number)
                    question = Questions.objects.get(pk=random_number, level=level)
                    answers = [question.answer1, question.answer2, question.answer3, question.correct_answer]
                    random.shuffle(answers)
                    return render_to_response('play_game.html', {'playing_question': question, 'answers': answers,
                                                                 'user': request.user, 'points': GameTactics.points,
                                                                 'ff_display': GameTactics.ff_display,
                                                                 'ra_display': GameTactics.ra_display,
                                                                 'remove_display': GameTactics.remove_display})
        else:
            create_game(request.user, cnt, level, GameTactics.points)
            return render_to_response('end_game.html', {'points': GameTactics.points, 'user': request.user})
