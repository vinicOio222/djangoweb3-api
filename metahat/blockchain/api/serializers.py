from rest_framework import serializers
from blockchain.models import Transaction, Wallet
from blockchain.services import Web3Service

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'sender_address', 'receiver_address', 'hash', 'amount')

    def create(self, validated_data):
        web3_service = Web3Service()
        sender_balance = web3_service.get_balance(validated_data['sender_address'])
        sender_wallet = Wallet.objects.get(public_address=validated_data['sender_address'])
        sender_key = sender_wallet.private_key
        if sender_balance < validated_data['amount']:
            raise serializers.ValidationError("Insufficient balance")
        
        hash = web3_service.transfer(
            validated_data['sender_address'],
            sender_key,
            validated_data['receiver_address'],
            validated_data['amount']
        )
        if hash:
            return super().create(
                {
                    'sender_address': sender_wallet,
                    'receiver_address': Wallet.objects.get(public_address=validated_data['receiver_address']),
                    'hash': hash,
                    'amount': validated_data['amount']
                }
            )
        else:
            raise serializers.ValidationError("Failed to send transaction")
    
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'user', 'public_address', 'balance')
    def to_representation(self, instance):
        web3_service = Web3Service()
        balance_in_weis = web3_service.get_balance(instance.public_address)
        balance_in_eth = web3_service.w3.from_wei(balance_in_weis, 'ether')
        instance.balance = balance_in_eth
        instance.save()
        return super().to_representation(instance)
