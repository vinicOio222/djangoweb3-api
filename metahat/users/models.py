from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, CharField, DateTimeField
from .managers import UserManager

class User(AbstractUser):
    username = CharField(max_length=255, unique=True, null=True, blank=False)
    email = EmailField(max_length=255, unique=True)
    access_expires_at = DateTimeField(null=True, blank=True)

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def get_wallets(self):
        return self.wallet_set.all()

    def get_transactions(self):
        return self.transaction_set.all()
