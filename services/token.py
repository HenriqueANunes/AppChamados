from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class MyTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        if user.is_template_user:
            raise serializers.ValidationError("Este usuário não tem permissão para fazer login.")

        return data
