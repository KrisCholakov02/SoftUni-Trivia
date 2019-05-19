from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Questions, Level


class LevelForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    points = forms.IntegerField(required=True, validators=[MinValueValidator(0), MaxValueValidator(1)])

    class Meta:
        model = Level
        fields = ('name', 'points')


class CreateQuestionForm(forms.ModelForm):
    question = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    correct_answer = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    answer1 = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    answer1 = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    answer2 = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    answer3 = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control ans-inp'
        }
    ))
    level = forms.ModelChoiceField(queryset=Level.objects.all(),
                                   widget=forms.Select(
                                       attrs={
                                           'class': 'form-control ans-inp'
                                       }
                                   ))

    class Meta:
        model = Questions
        fields = ('question', 'correct_answer', 'answer1', 'answer2', 'answer3', 'level')
