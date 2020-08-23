from rest_framework import serializers

from votes.models import User
from votes.serializers import AnswerFullSerializer

class UserSerializer(serializers.ModelSerializer):
    answers = AnswerFullSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'answers')
