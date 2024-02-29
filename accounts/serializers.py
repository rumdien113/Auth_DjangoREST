from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_of_birth', 'gender']

    def create(self, validated_data):
        user = Account(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            date_of_birth = validated_data['date_of_birth'],
            gender = validated_data['gender']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user