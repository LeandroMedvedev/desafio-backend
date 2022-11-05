from django.urls import path

from quizzes import views

app_name = 'quiz'

urlpatterns = [
    path('', views.QuizView.as_view(), name='list-quiz'),
    path(
        'random/<str:quiz_id>/',
        views.RandomQuestionsQuizView.as_view(),
        name='random-questions-quiz',
    ),
]