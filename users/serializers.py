from rest_framework import serializers
from preferences.models import Preference
from .models import UserProfile
from preferences.serializers import PreferenceSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=True),
    name = serializers.CharField(required=True),
    birth_date = serializers.CharField (required=True),
    phone = serializers.CharField(required=True)
    preferences = PreferenceSerializer(many=True, required=False)  # Permite crear y actualizar preferencias

    class Meta:
        model = UserProfile
        fields = ['user', 'name', 'birth_date', 'phone', 'preferences']
        extra_kwargs = {
            'user': {'write_only': True},  # Solo puedes escribir, no leer el campo 'user'
        }

    def create(self, validated_data):
        preferences_data = validated_data.pop('preferences', [])
        user = validated_data.pop('user', None)

        # Crea el perfil del usuario
        user_profile = UserProfile.objects.create(user=user, **validated_data)

        # Crea y asigna las preferencias si hay alguna
        for preference_data in preferences_data:
            preference, created = Preference.objects.get_or_create(**preference_data)
            user_profile.preferences.add(preference)

        return user_profile

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'birth_date', 'phone']
