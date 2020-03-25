from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class AccountManager(BaseUserManager):
    # Override 
    def create_user(self, email, username, password = None):
        # Campos obrigatorios
        if not email:
            raise ValueError("Usários devem ter um endereço de e-mail.")
        if not username:
            raise ValueError("Usários devem ter um nome de usuário (username).")

        user = self.model (
            email = self.normalize_email(email),
            username = username,
        )
        # Salvando
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Override
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username        = models.CharField(max_length = 30, unique = True)
    email           = models.EmailField(verbose_name="email", max_length = 100, unique = True)
    first_name      = models.CharField(max_length = 30)
    last_name       = models.CharField(max_length = 100)
    address         = models.CharField(max_length = 254)
    # Padrão models.User
    date_joined     = models.DateTimeField(verbose_name="Data de entrada", auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name="Ultimo login", auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'           # Usuários devem logar com email
    REQUIRED_FIELDS = ['email',]          # Campos obrigatorios

    objects = AccountManager()         # Gerenciador para criação das contas (Account)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None): 
        return self.is_admin

    def has_module_perms(self, app_label):
        return True # Sempre tem permissão

    class Meta:
        db_table = 'accounts_table'
        managed = True
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)