from rest_framework import generics, permissions, views, status
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserProfileSerializer
from .models import UserProfile
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.exceptions import NotFound


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
class UserProfileViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserProfileSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
   permission_classes = [permissions.IsAuthenticated]


   def post(self, request):
       try:
           token = Token.objects.get(user=request.user)
           token.delete()
           return Response({"message": "Token deleted"}, status=status.HTTP_200_OK)
       except Token.DoesNotExist:
           return Response({"message": "Token not found"}, status=status.HTTP_404_NOT_FOUND)

