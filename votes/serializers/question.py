from rest_framework import serializers

from votes.models import Question
from .answer import AnswerSerializer

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'name', 'description', 'date_created', 'date_closed', 'answers')
