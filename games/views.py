from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import generic

from .models import PlayedGames

# function that post the information of the played game
def create_game(user, number_of_questions, last_level, points):
    played_game = PlayedGames.objects.create(player=user, number_of_questions=number_of_questions,
                                             last_level=last_level, points=points)


# showing the games that the user has played
class UserGamesList(LoginRequiredMixin, generic.ListView):
    model = PlayedGames
    template_name = 'my_games_list.html'
    context_object_name = 'games'

# getting only user's played games
    def get_queryset(self):
        player_id = int(self.request.user.id)
        try:
            player = User.objects.all().filter(pk=player_id)[0]
            games = PlayedGames.objects.all().filter(player=player)
            return games
        except:
            return []
