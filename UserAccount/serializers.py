from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(unique=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        })
        return data

    def save(self, request):
        user = super().save(request)
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'date_joined', 'last_login']
        read_only_fields = ['id', 'date_joined', 'last_login']

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = [
            'id', 'email', 'first_name', 'last_name',
            'company', 'phone', 'address', 'website', 
            'bio', 'timezone', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class CustomPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password1'] != attrs['new_password2']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return attrs
