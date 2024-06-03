from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, UniqueConstraint
from users.models import User
from utils.models import BaseModel

class Wallet(BaseModel):
    user = ForeignKey(User, on_delete=CASCADE)
    public_address = CharField(max_length=255, unique=True)
    private_key = CharField(max_length=255, unique=True)
    balance = IntegerField(default=0)

    REQUIRED_FIELDS = [
        'user',
        'public_address',
        'private_key'
    ]

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'
        constraints = [
            UniqueConstraint(
                fields=["user"],
                name="You can have only one wallet per user.",
            ),
        ]

    def __str__(self):
        return self.public_address

    def get_balance(self) -> int:
        return self.balance

    def update_balance(self, amount: int) -> int:
        self.balance += amount
        self.save()
        return self.balance
    
    def list_transactions(self) -> list:
        return self.transaction_set.all()

class Transaction(BaseModel):
    sender_address = ForeignKey(Wallet, on_delete=CASCADE, to_field='public_address', related_name='sender')
    receiver_address = ForeignKey(Wallet, on_delete=CASCADE, to_field='public_address', related_name='receiver')
    amount = IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'
    
    def __str__(self):
        return f'{self.sender_address} -> {self.receiver_address}'
