from django.db.models import CharField, ForeignKey, CASCADE, IntegerField, UniqueConstraint
from metahat.models import BaseModel
from users.models import User

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
        constraint = [
            UniqueConstraint(
                fields=["user"],
                name="You can have only one wallet per user.",
            )
        ]

    def __str__(self):
        return self.public_address

    def get_balance(self) -> int:
        return self.balance

    def update_balance(self, amount: int) -> int:
        self.balance += amount
        self.save()
        return self.balance

