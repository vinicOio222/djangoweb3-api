from rest_framework import serializers
from blockchain.models import Transaction, Wallet
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'sender_address', 'receiver_address', 'amount']

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['id', 'user', 'public_address', 'private_key', 'balance']