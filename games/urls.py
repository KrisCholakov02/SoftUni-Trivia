from django.urls import path

from . import views

urlpatterns = [
    path('mine/', views.UserGamesList.as_view(), name='my-games'),
]