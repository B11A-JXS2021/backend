from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class UserInfo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(User.objects.values().get(email=request.user.email), status=status.HTTP_200_OK)

    def put(self, request):
        try:
            email = request.user.email
            user_obj = User.objects.get(email=email)
            user_obj.blood = request.data.get('blood')
            user_obj.emergency = request.data.get('emergency')
            user_obj.disease = request.data.get('disease')
            user_obj.medicine = request.data.get('medicine')
            print(user_obj)
            user_obj.save()
            return Response("User was Updated", status=status.HTTP_200_OK)
        except:
            return Response("Update failed", status=status.HTTP_400_BAD_REQUEST)
