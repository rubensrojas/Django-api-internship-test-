from rest_framework import serializers
from .models import Account


class RegistrarionSerializer(serializers.ModelSerializer):
    # Novo field, write_only=True não deixa ver o input
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'address']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            address = self.validated_data['address'],
        )
        password  = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Senhas devem ser iguais.'})
        account.set_password(password)
        account.save()
        return account
        