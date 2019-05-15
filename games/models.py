from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator

from questions.models import Level


class PlayedGames(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_questions = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(15)], default=0)
    last_level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=False)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Player:{self.player.username} answered {self.number_of_questions} questions and the game ended on {self.last_level.name} leve."
