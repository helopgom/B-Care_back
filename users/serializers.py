from rest_framework import serializers
from preferences.models import Preference
from .models import UserProfile
from preferences.serializers import PreferenceSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','username','id','birth_date', 'phone', 'preferences']


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
    birth_date = serializers.DateField(format='%d-%m-%Y', input_formats=['%Y-%m-%d'])
    class Meta:
        model = UserProfile
        fields = ['first_name', 'birth_date', 'phone']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d', '%d-%m-%Y'], required=False)
    phone = serializers.CharField(max_length=15, required=False)

    class Meta:
        model = UserProfile
        fields = ['first_name', 'birth_date', 'phone']

    def update(self, instance, validated_data):
        # Iterar sobre los campos y actualizar solo los que fueron proporcionados
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
