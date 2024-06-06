from rest_framework import serializers
from users.models import User
from blockchain.api.serializers import WalletSerializer

class UserSerializer(serializers.ModelSerializer):
    wallets = WalletSerializer(source='wallet_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'wallets')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user, _ = User.objects.create_user_and_wallet(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user
