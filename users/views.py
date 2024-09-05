from rest_framework import generics, permissions, views, status
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserProfileSerializer
from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
class UserProfileViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserProfileSerializer
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
    # Devolver solo el perfil del usuario autenticado
        return UserProfile.objects.filter(user=self.request.user)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(views.APIView):
   permission_classes = [permissions.IsAuthenticated]


   def post(self, request):
       try:
           token = Token.objects.get(user=request.user)
           token.delete()
           return Response({"message": "Token deleted"}, status=status.HTTP_200_OK)
       except Token.DoesNotExist:
           return Response({"message": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)

