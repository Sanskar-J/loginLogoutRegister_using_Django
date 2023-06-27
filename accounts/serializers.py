from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import CustomUser

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'phone_number', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        
        user = User.objects.create_user(username= validated_data['phone_number'],email= validated_data['email'],password= validated_data['password'])

        return user

class SecretSerializer(serializers.ModelSerializer):
    class Meta:
        model=  User
        fields=('username','password')