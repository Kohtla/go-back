from rest_framework import serializers

from votes.models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'question', 'amount')
        extra_kwargs = {
            'question': {'write_only': True}
        }


    def create(self, validated_data):
        return Answer.objects.create(**validated_data)


class AnswerFullSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'text', 'question', 'question_name')
