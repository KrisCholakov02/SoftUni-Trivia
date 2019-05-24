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

    # function for the joker '50/50'
    def fifty_fifty(request, pk):
        if GameTactics.ff_display:  # checking if the joker is used
            question = Questions.objects.get(pk=pk)  # gets playing question
            correct_answer = question.correct_answer  # gets the correct answer
            answers = [question.answer1, question.answer2, question.answer3]  # makes list of other answers
            random_number = random.randint(0, 2)
            other_answer = answers[random_number]  # choosing one of the other answers
            f_answers = [correct_answer, other_answer]  # making list of the correct one and other one
            random.shuffle(f_answers)  # shuffling so not to guess
            GameTactics.ff_display = False  # changing the variable so not to show the joker button again
            return render_to_response('play_game.html', {'playing_question': question, 'answers': f_answers,
                                                         'user': request.user, 'points': GameTactics.points,
                                                         'ff_display': GameTactics.ff_display,
                                                         'ra_display': GameTactics.ra_display,
                                                         'remove_display': GameTactics.remove_display})

    # function for the joker 'right answer'
    def right_answer(request, pk):
        if GameTactics.ra_display:  # checking if the joker is used
            question = Questions.objects.get(pk=pk)  # gets playing question
            correct_answer = question.correct_answer  # gets the correct answer
            answers = [correct_answer]  # making list only from the correct answer
            GameTactics.ra_display = False  # changing the variable so not to show the joker button again
            return render_to_response('play_game.html', {'playing_question': question, 'answers': answers,
                                                         'user': request.user, 'points': GameTactics.points,
                                                         'ff_display': GameTactics.ff_display,
                                                         'ra_display': GameTactics.ra_display,
                                                         'remove_display': GameTactics.remove_display})

    # function for the joker 'remove answer'
    def remove_answer(request, pk):
        if GameTactics.remove_display:  # checking if the joker is used
            question = Questions.objects.get(pk=pk)  # gets playing question
            correct_answer = question.correct_answer  # gets the correct answer
            answers = [question.answer1, question.answer2, question.answer3]  # makes list of other answers
            random.shuffle(answers)
            answers.remove(answers[2])  # remove one of the other answers
            answers.append(correct_answer)  # appending the correct one to the list
            random.shuffle(answers)  # shuffling so not to guess
            GameTactics.remove_display = False  # changing the variable so not to show the joker button again
            return render_to_response('play_game.html', {'playing_question': question, 'answers': answers,
                                                         'user': request.user, 'points': GameTactics.points,
                                                         'ff_display': GameTactics.ff_display,
                                                         'ra_display': GameTactics.ra_display,
                                                         'remove_display': GameTactics.remove_display})

    def start_game(request):
        GameTactics.played_questions_pks = []  # setting variable to its default value
        GameTactics.points = 0  # setting variable to its default value
        GameTactics.ff_display = True  # setting variable to its default value
        GameTactics.ra_display = True  # setting variable to its default value
        GameTactics.remove_display = True  # setting variable to its default value
        while True:
            random_number = random.randint(1, Questions.objects.all().filter(checked=1).order_by('-id')[0].id)
            # getting random number from 1 to Questions DB's length
            if random_number in GameTactics.played_questions_pks:
                # checking if the number is not already chosen
                continue
            else:
                try:
                    question = Questions.objects.get(pk=random_number)  # getting random question
                    if question.level == Level.objects.get(pk=1):
                        answers = [question.answer1, question.answer2, question.answer3, question.correct_answer]
                        # making list of all answers
                        random.shuffle(answers)  # shuffling so not to guess
                        GameTactics.played_questions_pks.append(random_number)
                        # appending the number(pk) to played ones
                        return render_to_response('play_game.html', {'playing_question': question, 'answers': answers,
                                                                     'user': request.user, 'points': GameTactics.points,
                                                                     'ff_display': GameTactics.ff_display,
                                                                     'ra_display': GameTactics.ra_display,
                                                                     'remove_display': GameTactics.remove_display})
                    else:
                        continue
                except:
                    continue

    def next_question(request, pk, correct):
        level_err = False
        question = Questions.objects.get(pk=pk)  # gets playing question
        cnt = len(GameTactics.played_questions_pks)  # getting the number of played questions
        # logic for changing the level during the game
        if 0 <= cnt < 5:
            level = Level.objects.get(pk=1)  # changing the level
        elif 5 <= cnt < 10:
            level = Level.objects.get(pk=2)  # changing the level
        elif 10 <= cnt < 15:
            level = Level.objects.get(pk=3)  # changing the level
        elif cnt == 15:
            level = 'end'
        else:
            level_err = True
        # ending the game while done some bugs
        if level_err:
            create_game(request.user, cnt, level, GameTactics.points)
            return render_to_response('end_game.html', {'points': GameTactics.points, 'user': request.user})
        # if everything is OK
        if level == 'end':  # if the player has done all the questions
            GameTactics.points += question.level.points  # increasing points with the current for the level
            level = Level.objects.get(pk=3)  # setting the level to the maximum one
            create_game(request.user, cnt, level, GameTactics.points)  # posting the played game information
            return render_to_response('end_game.html', {'points': GameTactics.points, 'user': request.user})
        elif correct == '1':  # if the chosen answer is correct
            GameTactics.points += question.level.points  # increasing points with the current for the level
            while True:
                random_number = random.randint(1, Questions.objects.all().filter(checked=1).order_by('-id')[0].id)
                # getting random number from 1 to Questions DB's length
                if random_number in GameTactics.played_questions_pks:
                    # checking if the number is not already chosen
                    continue
                else:
                    try:
                        question = Questions.objects.get(pk=random_number)  # getting random question
                        if question.level == level:
                            answers = [question.answer1, question.answer2, question.answer3, question.correct_answer]
                            # making list of all answers
                            random.shuffle(answers)  # shuffling so not to guess
                            GameTactics.played_questions_pks.append(random_number)
                            # appending the number(pk) to played ones
                            return render_to_response('play_game.html',
                                                      {'playing_question': question, 'answers': answers,
                                                       'user': request.user, 'points': GameTactics.points,
                                                       'ff_display': GameTactics.ff_display,
                                                       'ra_display': GameTactics.ra_display,
                                                       'remove_display': GameTactics.remove_display})
                        else:
                            continue
                    except:
                        continue
        # preventing unknown bugs
        else:
            create_game(request.user, cnt, level, GameTactics.points)
            return render_to_response('end_game.html', {'points': GameTactics.points, 'user': request.user})
