from rest_framework import serializers
from .models import UserProfile
from preferences.serializers import PreferenceSerializer  # Asegúrate de importar tu PreferenceSerializer
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
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