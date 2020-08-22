from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from votes.models import User
from votes.serializers import UserSerializer

class UserView(APIView):

    def post(self, request):
        name = request.data.get('name', None)
        if name:
            user, created = User.objects.get_or_create(name=name)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"need some name"}, status=status.HTTP_400_BAD_REQUEST)