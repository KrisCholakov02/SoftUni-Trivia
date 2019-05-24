from django.db import models
from django.core.validators import MinValueValidator, MaxLengthValidator, MaxValueValidator

from accounts.models import ProfileUser
# Create your models here.


class Level(models.Model):
    name = models.CharField(max_length=30)
    points = models.PositiveIntegerField(validators=[MinValueValidator(10)])

    def __str__(self):
        return f"{self.name}"


class Questions(models.Model):
    author = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    question = models.CharField(max_length=350)
    correct_answer = models.CharField(max_length=150)
    answer1 = models.CharField(max_length=150)
    answer2 = models.CharField(max_length=150)
    answer3 = models.CharField(max_length=150)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=False)
    checked = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)

    def __str__(self):
        return f"Question:{self.pk} is {self.level.name} with {self.level.points}"
