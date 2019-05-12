import django
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('profile/', views.redirect_user, name='profile'),
    re_path('profile/(?P<pk>\d+)/', views.UserDetail.as_view(), name='profile-user'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    re_path('^edit/(?P<pk>\d+)/$', views.ProfileUserEdit.as_view(), name='profile-edit'),
]