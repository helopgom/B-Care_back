from .models import UserProfile
from django.contrib.auth.models import User
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta: model = User
    fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format='%d-%m-%Y', input_formats=['%Y-%m-%d'])
    class Meta:
        model = UserProfile
        fields = ['id','name', 'birth_date', 'phone', 'preferences']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    phone = serializers.CharField(write_only=True, required=True)
    name = serializers.CharField(write_only=True, required=True)
    birth_date = serializers.DateField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'phone', 'name', 'birth_date']  # Añadimos phone a los campos

    def create(self, validated_data):
        # Primero, creamos el usuario
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        # Luego, creamos el perfil de usuario y asignamos el campo 'phone'
        UserProfile.objects.create(
            user=user,  # Relacionamos el perfil con el usuario
            phone=validated_data['phone'],
            name=validated_data['name'],
            birth_date=validated_data['birth_date']
        )

        return user
