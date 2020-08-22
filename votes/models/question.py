from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField()

    def __str__(self):
        return self.name
