from django.urls import path, re_path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='game_home.html'), name='home'),
    path('play/', views.GameTactics.start_game, name='play'),
    re_path('^fifty-fifty/(?P<pk>\d+)/$', views.GameTactics.fifty_fifty, name='fifty-fifty'),
    re_path('^right-answer/(?P<pk>\d+)/$', views.GameTactics.right_one, name='right-answer'),
    re_path('^remove-answer/(?P<pk>\d+)/$', views.GameTactics.remove_one, name='remove-answer'),
]