from hashlib import blake2b

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('Email can not be empty')
        email = self.normalize_email(email)
        print(extra_fields)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    class UserTypes(models.Choices):
        RESTAURANT = 1
        CUSTOMER = 2
        COURIER = 3

    username = None
    nickname = models.CharField(max_length=254)
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)  # changes email to unique and blank to false
    objects = UserManager()
    tenant_type = models.IntegerField(choices=UserTypes.choices, default=UserTypes.CUSTOMER)

    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


class Token(models.Model):
    value = models.CharField(max_length=254)
    create_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('User', models.CASCADE)
    active = models.BooleanField(default=True)
    expiration_time_in_hours = 24

    class Meta:
        abstract = True

    def generate_value(self):
        hashes = blake2b()
        hashes.update("{0}{1}{2}".format('kfklJ3!svs+sdff', timezone.now(), 'LKJ=(GJHSDWE2345t').encode())
        self.value = hashes.hexdigest()
        self.save()

    def is_active(self):
        now = timezone.now()
        # 2018-01-25 10:25 - 2018-01-25 10:10
        return self.active and (
            now - self.create_date).seconds < 60 * 60 * self.expiration_time_in_hours  # 24 óráig érvényes a token


class PasswordResetToken(Token):
    expiration_time_in_hours = 4
