from django.contrib.auth.models import UserManager as DjangoUserManager
from django.contrib.auth.hashers import make_password
from utils.encryption import Encryption

class UserManager(DjangoUserManager):
    def _create_user(self, email: str, password: str, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_user_and_wallet(self, first_name: str, last_name: str, email: str, password: str) -> tuple:
        from blockchain.models import Wallet
        username = f'@{first_name.lower()}_{Encryption.generate_key(7)}'
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        Wallet.objects.create(
            user=user,
            
            )

        return user

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
