from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from votes.models import Question
from votes.serializers import QuestionSerializer

class QuestionView(APIView):

    def get(self, request):
        objects = Question.objects.all()
        serializer = QuestionSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

