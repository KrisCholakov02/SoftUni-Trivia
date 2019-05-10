from django.urls import path, re_path, include
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('mine/', views.UserQuestionsList.as_view(), name='my_questions'),
    re_path('^create/$', views.QuestionCreate.as_view(), name='create_question'),
    re_path('^details/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='question-detail'),
    re_path('^delete/(?P<pk>\d+)/$', views.QuestionDelete.as_view(), name='question-delete'),
    re_path('^edit/(?P<pk>\d+)/$', views.QuestionEdit.as_view(), name='question-edit'),

]