from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.apioverview, name = 'api-overview'),
    path('topics/', views.quiztopics, name = 'quiz-topics'),
    path('topics/<str:pk>/', views.quizsubtopics, name = 'quiz-subtopics'),
    path('questions/', views.quizquestions, name = 'quiz-questions'),
    path('questions/<str:pk>/', views.quiztopicquestions, name = 'quiztopicquestions'),
    path('subtopics/questions/<str:pk>/', views.quizsubtopicquestions, name = 'quizsubtopicquestions'),
]