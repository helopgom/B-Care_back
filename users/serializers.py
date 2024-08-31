from rest_framework import serializers
from .models import UserProfile
#from preferences.serializers import PreferenceSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    birth_date = serializers.StringRelatedField()
    phone = serializers.StringRelatedField()
    #preferences = PreferenceSerializer(many=True)  # Incluir preferencias

    class Meta:
        model = UserProfile
        fields = ['user', 'birth_date', 'phone', 'preferences']