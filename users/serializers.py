from rest_framework import serializers      #new


class SignUpSerializer(serializers.Serializer):      #new
    email = serializers.EmailField()      #new
    password = serializers.CharField()      #new
    password2 = serializers.CharField()      #new


class TokenSerializer(serializers.Serializer):      #new
    email = serializers.EmailField()      #new
    password = serializers.CharField()      #new


class RefreshTokenSerializer(serializers.Serializer):      #new
    refresh = serializers.EmailField()      #new


class PasswordChangeSerializer(serializers.Serializer):      #new
    old_password = serializers.CharField()      #new
    password = serializers.CharField()      #new
    password2 = serializers.CharField()      #new