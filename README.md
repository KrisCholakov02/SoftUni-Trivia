# Trivia
Docummentation: https://drive.google.com/drive/folders/1Yzf1batvcAsdExkMGkElrIKno5U6IzTq?usp=sharing

URLS:<br>
path('admin/', admin.site.urls)  # going to admin panel<br>
path('accounts/', include('accounts.urls')),  # linking functions connected with users<br>
path('game/', include('game.urls')),  # linking functions for game tactics<br>
path('questions/', include('questions.urls')),  # linking the functions for editing, showing, deleting, etc question<br>
path('games/', include('games.urls')),  # linking functions connected with played games<br>
re_path(r'^$', TemplateView.as_view(template_name='game_home.html'), name='home'),  # setting home page
