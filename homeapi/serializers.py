from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import date
from django.core.exceptions import ValidationError

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password', 
            'password2', 
            'full_name', 
            'phone_number', 
            'date_of_birth', 
            'address', 
            'profile_picture', 
            'user_type'
        ]
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_email(self, value):
        # ตรวจสอบอีเมลให้เป็นไปตามรูปแบบ
        if not value or "@" not in value or "." not in value.split("@")[-1]:
            raise serializers.ValidationError("Please provide a valid email address.")
        return value

    def validate_date_of_birth(self, value):
        if value > date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)  # Create user with validated data
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'phone_number', 
            'date_of_birth', 
            'address', 
            'profile_picture', 
            'user_type'
        ]
