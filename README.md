# Trivia
Docummentation: https://drive.google.com/drive/folders/1Yzf1batvcAsdExkMGkElrIKno5U6IzTq?usp=sharing

URLS:
path('admin/', admin.site.urls)  # going to admin panel
path('accounts/', include('accounts.urls')),  # linking functions connected with users
path('game/', include('game.urls')),  # linking functions for game tactics
path('questions/', include('questions.urls')),  # linking the functions for editing, showing, deleting, etc question
path('games/', include('games.urls')),  # linking functions connected with played games
re_path(r'^$', TemplateView.as_view(template_name='game_home.html'), name='home'),  # setting home page
