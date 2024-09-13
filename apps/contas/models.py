from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group, Permission

class GestaoUsuario(BaseUserManager):
    def create_user(self, cpf, email=None, password=None, **extra_fields):
        if not cpf:
            raise ValueError('O CPF deve ser fornecido.')
        user = self.model(cpf=cpf, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(cpf, email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length=14, unique=True, db_index=True)
    name = models.CharField(max_length=255, null=False, blank=False, db_index=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='usuario_set', blank=True)
    user_permissions = models.ManyToManyField(Permission,related_name='usuario_user_permissions_set', blank=True)
    objects = GestaoUsuario()
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.cpf
