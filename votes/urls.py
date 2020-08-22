from django.urls import path

from .views import QuestionView, AnswerView

app_name = 'votes'

urlpatterns = [
    path('', QuestionView.as_view(), name='question_view'),
    path('/answers', AnswerView.as_view(), name='answer_view')
]
