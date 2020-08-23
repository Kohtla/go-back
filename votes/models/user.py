from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)

    @property
    def answers(self):
        return self.answers

    def __str__(self):
        return self.name
