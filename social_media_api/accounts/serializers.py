# accounts/serializers.py
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source="followers_count", read_only=True)
    following_count = serializers.IntegerField(source="following_count", read_only=True)

    class Meta:
        model = User
        fields = [
            "id", "username", "email", "first_name", "last_name",
            "bio", "profile_picture", "followers_count", "following_count"
        ]
        read_only_fields = ["id", "followers_count", "following_count"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "token"]

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        token, _ = Token.objects.get_or_create(user=instance)
        data["token"] = token.key
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs.get("username"), password=attrs.get("password")
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key}


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "bio", "profile_picture"]
