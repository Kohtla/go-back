from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from votes.models import User, Answer
from votes.serializers import UserSerializer

class VoteView(APIView):

    def post(self, request):
        answer_id = request.data.get('answer', None)
        user_id = request.data.get('user', None)
        answer = Answer.objects.get(id=answer_id)
        user = User.objects.get(id=user_id)

        answer.users.add(user)
        answer.save()

        return Response(status=status.HTTP_200_OK)
