from django.urls import path 
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
   path('', views.home, name = 'home'),
   path('about/', views.about, name = 'about'),
   path('mainmenu/', views.mainmenu, name = 'mainmenu'),
   path('topics/<str:pk>/', views.subtopics, name = 'subtopics'),
   path('instructions/<str:pk>/', views.instructionpage, name = 'instructions'),
   path('subtopics/questions/<str:pk>/', views.questionspersubtopic, name = 'questionsubtopic'),
   path('questionform/', views.questionform, name = 'question-form'),
   path('score/<str:pk>/', views.score, name = 'score'),
   path('scorecard/', views.scorecard, name = 'scorecard'),
   path('view_scores/<str:pk>/', views.viewscores, name = 'viewscores'),
   path('userprofile/', views.userprofile, name = 'userprofile'),
   path('editprofile/', views.updateprofile, name = 'update-profile'),
   path('login/', views.loginpage, name = 'loginuser'),
   path('logout/', views.logoutpage, name = 'logoutuser'),
   path('register/', views.registeruser, name = 'registeruser'),
   path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'quizapp/password_reset.html'), name = 'password_reset'),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='quizapp/password_reset_done.html'), name = 'password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'quizapp/password_reset_confirm.html'), name = 'password_reset_confirm'),
   path('password-reset-complete/',
      auth_views.PasswordResetCompleteView.as_view(
         template_name = 'quizapp/password_reset_complete.html'
      ),
      name = 'password_reset_complete'),
]