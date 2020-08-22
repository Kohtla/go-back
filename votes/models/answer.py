from django.db import models

from .question import Question
from .user import User

class Answer(models.Model):
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    users = models.ManyToManyField(User, related_name='answers')

    def __str__(self):
        return self.text
