from django.urls import path, re_path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='game_home.html'), name='home'),
    path('play/', views.get_question, name='play')
]